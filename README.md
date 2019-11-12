# Image Resizer

### Usage
```
image_resizer.py [-h] [--drop_loc path] [--new_name name] new_width new_height old_image_path
```
```
positional arguments:
      new_width           Width of the new image in px
      new_height          Height of the new image in px
      old_image_path      Path to image

optional arguments:
      -h, --help          show this help message and exit
      --drop_loc  path    Path to where to save the new image. The default is on
                          computer temp directory.
      --new_name  name    New resized image name, by default the name will be
                          <old_name>_resized.
```
### Example
```
      python test/image_resizer.py 150 150 /home/rexy.jpg
      python test/image_resizer.py 150 150 /home/rexy.jpg --drop_loc /home/resized/ --new_name young_rexy.jpg
```

### Image resizer can be found [here](client/image_resizer.py)
#### The module recieves a path to an image's width, height and saves the new resized image to ```<drop_loc>``` with the new width and height provided.

# Image Resizer Test
### Usage
```
test_resize.py [-h] [--max_gpu percent1-100] N M video_path
```
```
positional arguments:
      N           Number of instances
      M           Delay to start next proccess
      video_path  Local path to video

optional arguments:
      -h, --help            show this help message and exit
      --max_gpu   percent   Maximum gpu usage while processing video.
```
### Example
```
python ./test/test_resize.py 2 10 ./test/videosample.mp4
```

### Image resizer test can be found [here](test/test_resize.py)
#### The module recieves the N, M values and a video and makes N instances that contain the video frame, resized - with M delay between each instance.
