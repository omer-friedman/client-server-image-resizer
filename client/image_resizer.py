from argument_parser import ArgumentParser
import sys
import requests
import os
import numpy as np
import json
import cv2
import imghdr

allowed_extensions = ['jpg', 'jpeg', 'png']
host = 'http://localhost'
port = 5000
api_image_resize_endpoint = '/api/resize_image'


def main():
    args = ArgumentParser().args
    image_path = args.image_path

    address = host + ":" + str(port)
    # task_resize_addr = address + '/api/new_task'
    one_resize_addr = address + api_image_resize_endpoint

    if not is_valid_image(image_path):
        print("Error: Invalid image path {}".format(image_path), file=sys.stderr)
        exit(1)

    new_image_name, image_extension = get_new_image_name(image_path, args.new_name)
    files = prepare_image_package_to_send(image_path, args.new_width, args.new_height)
    response = requests.post(one_resize_addr, files=files)
    nparr = np.frombuffer(response.content, np.uint8)
    new_sized_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    file_drop_loc = args.drop_loc + new_image_name + "." + image_extension
    save_new_resized_image(new_sized_image, file_drop_loc)


def is_valid_image(image_path):
    """
    Parameters
    ----------
    :param image_path : String
        full path to image

    returns True if the image exists and is legal (has legal extension), False otherwise
    """
    try:
        if imghdr.what(image_path) not in allowed_extensions:
            return False
    except Exception as e:
        return False

    return True


def get_new_image_name(image_path, image_name):
    """
    Parameters
    ----------
    :param image_path : String
        full path to image
    :param image_name : String
        image name from module arguemnt

    returns the new image name and extension according to arguments provided.
    """
    extension = image_path[image_path.rfind(".") + 1:]
    if image_name:
        if image_name.rfind(".") != -1:
            return image_name[:image_name.rfind(".")], extension
        return image_name, extension
    name_addition = "_resized"
    image_name = image_path[image_path.rfind(os.sep) + 1:image_path.rfind(".")] + name_addition
    return image_name, extension


def prepare_image_package_to_send(img_path, new_width, new_height):
    """
    Parameters
    ----------
    :param img_path : String
        full path to image
    :param new_width : int
        width for the new image
    :param new_height : int
        height for the new image

    returns file block contains the image encoded and the new image properties.
    """
    image_new_prop = {'new_width': new_width, 'new_height': new_height}
    img = cv2.imread(img_path)
    img_encoded = cv2.imencode('.jpg', img)[1]
    files = [
        ('image', ('image', img_encoded.tostring(), 'image/jpeg')),
        ('datas', ('datas', json.dumps(image_new_prop), 'application/json'))
    ]
    return files


def save_new_resized_image(new_sized_image, file_drop_loc):
    """
    Parameters
    ----------
    :param new_sized_image : numpy.ndarray
        image as ndarray ready to save.
    :param file_drop_loc : String
        width for the new image.

    returns file block contains the image encoded and the new image properties.
    """
    try:
        cv2.imwrite(file_drop_loc, new_sized_image)
        print("Image saved to: {}".format(file_drop_loc))
    except Exception as e:
        print("Error: Couldn't save image to {}.\n{}".format(file_drop_loc, e))


if __name__ == "__main__":
    main()
