# Batch-Image-Cropper
python3 code for cropping a specific rectangular area from all images in a folder

required python packages: **os, cv2, tqdm**<br>
os is pre-installed with python<br>
to install others: `pip3 install opencv-python tqdm`<br>
if pip ins't installed: `sudo apt-get install python3-pip`<br>

to use the code, run the command:<br>
&nbsp;&nbsp;&nbsp;&nbsp; `python3 cropper.py` <br>

Use the *Sample code* to finalize rectange dimensions by adjusting row\_start, row\_end, col\_start, col\_end vairables<br>
(You can use `xdotool getmouselocation` to get estimates for x-y coordinates to use for above variables)<br>
Once satisfied, comment the *Sample code* and uncommment the *Final code* and run it.
