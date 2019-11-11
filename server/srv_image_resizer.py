from flask import Flask, request, make_response
import numpy as np
import cv2
import json
import redis
from rq import Queue


app = Flask(__name__)
red = redis.Redis()
que = Queue(connection=red)


@app.route('/api/resize_image', methods=['POST'])
def handle_resize_request(image_encode="", image_props="", multitask=False):
    if not multitask:
        image_encode = request.files['image'].read()
        image_props = json.load(request.files['datas'])
    nparr = np.frombuffer(image_encode, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    dim = (image_props['new_width'], image_props['new_height'])
    resized_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    resized_img_encoded = cv2.imencode('.jpg', resized_img)[1]
    response = make_response(resized_img_encoded.tobytes())
    response.headers.set('Content-Type', 'image/jpeg')
    return response


@app.route('/api/new_task', methods=['POST'])
def add_new_resize_task_to_queue():
    try:
        image_encode = request.files['image'].read()
        image_props = json.load(request.files['datas'])
        response = que.enqueue(handle_resize_request, image_encode, image_props, multitask=True)
    except Exception as e:
        response = {'message': "Bad request - {}".format(e)}

    return make_response(response.tobytes())


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
    # app.run()
