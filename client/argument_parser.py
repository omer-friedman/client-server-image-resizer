import argparse
import tempfile
import os


class ArgumentParser:
    parser = argparse.ArgumentParser(description='The module will get a path to image and will save it to <drop_loc> with the new width and height provided')
    parser.add_argument('new_width', metavar='new_width', type=int, help='Width of the new image in px')
    parser.add_argument('new_height', metavar='new_height', type=int, help='Height of the new image in px')
    parser.add_argument('image_path', metavar='old_image_path', type=str, help='Path to image')
    tempdir = tempfile.gettempdir()+os.sep
    parser.add_argument('--drop_loc', metavar='path', type=str, help='Path to where to save the new image. The default is on {}'.format(tempdir, os.sep), default=tempdir)
    parser.add_argument('--new_name', metavar='name', type=str, help='New resized image name')
    args = parser.parse_args()
