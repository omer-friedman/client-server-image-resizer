# __Image Resizer__
To use the Image Resizer go to client/image_resizer.py<br />
The module will get a path to image, width and height and will save the<br />
new resized image to <drop_loc> with the new width and height provided.<br />

__usage:__<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;image_resizer.py [-h] [--drop_loc path] [--new_name name] new_width new_height old_image_path<br />
__e.g:__<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python test/image_resizer.py 150 150 /home/rexy.jpg<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python test/image_resizer.py 150 150 /home/rexy.jpg --drop_loc /home/resized/ --new_name young_rexy.jpg

__positional arguments:__<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new_width&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Width of the new image in px<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new_height&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Height of the new image in px<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;old_image_path&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Path to image

__optional arguments:__<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-h, --help&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;show this help message and exit<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--drop_loc&nbsp;&nbsp;path&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Path to where to save the new image. The default is on<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;computer temp directory.<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--new_name&nbsp;&nbsp;name&nbsp;&nbsp;New resized image name, by default the name will be<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<old_name>_resized.<ext>



# __Image Resizer Test__
To use the image resizer test go to test/test_resize.py

__usage:__<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;test_resize.py [-h] [--max_gpu percent1-100] N M video_path<br />
__e.g:__<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python ./test/test_resize.py 2 10 ./test/videosample.mp4

The module will get an N, M and a video and will make N instances that contain<br />
the video frame, resized - with M delay between each instance.

__positional arguments:__<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number of instances<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Delay to start next proccess<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;video_path&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Local path to video

__optional arguments:__<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-h, --help&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;show this help message and exit<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--max_gpu&nbsp;&nbsp;percent&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Maximum gpu usage while processing video.<br />
