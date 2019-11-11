import time
from test_argument_parser import ArgumentParser
import cv2
import os
import threading
import tempfile


def main():
    args = ArgumentParser.args
    n = args.N
    m = args.M
    max_gpu = args.max_gpu
    vid_path = args.video_path
    for i in range(n):
        msg = "* Start processing instance {} *".format(i + 1)
        print("*" * len(msg))
        print(msg)
        print("*" * len(msg))
        wait_until_gpu_usage_free(max_gpu)  # Barrier
        ins_thread = threading.Thread(target=save_video_as_resized_images, args=(vid_path, i+1))
        ins_thread.start()
        if i + 1 <= n:
            print("Sleeping for " + str(m) + " seconds.")
            time.sleep(m)


def save_video_as_resized_images(vid_path, instance):
    """
    Parameters
    ----------
    :param vid_path:  String
        full path to video path
    :param instance : int
        number of the current instance

    returns file block contains the image encoded and the new image properties.
    """
    temp_folder = tempfile.gettempdir() + os.sep
    directory = temp_folder + "vid-instance" + str(instance) + os.sep
    if not os.path.exists(directory):
        os.makedirs(directory)
    vid_cap = cv2.VideoCapture(vid_path)
    success, image = vid_cap.read()
    count = 1
    while success:
        current_file_name = "Frame{}.jpg".format(str(count).zfill(5))
        full_path = directory + current_file_name
        cv2.imwrite(full_path, image)
        # Resized image will replace the original frame image because of same image path.
        os.system("..{0}client{0}image_resizer.py 40 40 {1} --drop_loc {2} --new_name {3}".format(os.sep, full_path, directory, current_file_name))
        success, image = vid_cap.read()
        count += 1
    return []


def wait_until_gpu_usage_free(max_usage):
    """
    Parameters
    ----------
    :param max_usage:  int
        maximum usage of the gpu.
        if the current gpu usage is higher than max_usage, the current
        resize task will wait for the gpu usage to decrease.

    """
    # TODO get GPU usage and check if it under the maximum usage. If it is, return true, else wait for it to be true. (interval, timeout)
    return True


if __name__ == '__main__':
    main()
