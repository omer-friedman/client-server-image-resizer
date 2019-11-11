from argument_parser import ArgumentParser
import requests
import os
import numpy as np
import json
import cv2
import imghdr

allowed_extensions = ["jpg", "jpeg", "png"]


def main():
    args = ArgumentParser().args
    new_width = args.new_width
    new_height = args.new_height
    image_name = args.new_name
    drop_loc = args.drop_loc
    image_path = args.image_path
    address = 'http://localhost:5000'
    # task_resize_addr = address + '/api/new_task'
    one_resize_addr = address + '/api/resize_image'
    check_image_path(image_path)
    new_image_name, image_extension = decide_new_image_name(image_path, image_name)
    # drop_loc, new_image_name = get_correct_drop_loc(drop_loc, image_name, image_extenstion)
    files = prepare_image_package_to_send(image_path, new_width, new_height)
    response = requests.post(one_resize_addr, files=files)
    nparr = np.frombuffer(response.content, np.uint8)
    new_sized_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    file_drop_loc = drop_loc+new_image_name+"."+image_extension
    save_new_resized_image(new_sized_image, file_drop_loc)


def check_image_path(image_path):
    message = ""
    try:
        if imghdr.what(image_path) not in allowed_extensions:
            message = "ERROR: Image extension must be jpeg, jpg or png"
    except Exception as e:
        message = str(e)

    if message:
        print(message)
        exit(1)


def decide_new_image_name(image_path, full_name):
    extension = image_path[image_path.rfind(".")+1:]
    if full_name:
        if full_name.rfind(".") != -1:
            return full_name[:full_name.rfind(".")], extension
        return full_name, extension
    image_name = image_path[image_path.rfind(os.sep)+1:image_path.rfind(".")]+"_resized"
    return image_name, extension


def prepare_image_package_to_send(img_path, new_width, new_height):
    image_new_prop = {'new_width': new_width, 'new_height': new_height}
    img = cv2.imread(img_path)
    img_encoded = cv2.imencode('.jpg', img)[1]
    files = [
        ('image', ('image', img_encoded.tostring(), 'image/jpeg')),
        ('datas', ('datas', json.dumps(image_new_prop), 'application/json'))
    ]
    return files


def save_new_resized_image(new_sized_image, file_drop_loc):
    try:
        cv2.imwrite(file_drop_loc, new_sized_image)
        print("Image saved to: {}".format(file_drop_loc))
    except Exception as e:
        print("Error: Couldn't save image to {}.\n{}".format(file_drop_loc, e))


if __name__ == "__main__":
    main()
