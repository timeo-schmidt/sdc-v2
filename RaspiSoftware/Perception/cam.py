# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
from datetime import datetime
import numpy as np
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 90
camera.hflip = True
camera.shutter_speed = 200
camera.vflip = True
camera.brightness = 50

rawCapture = PiRGBArray(camera, size=(640, 480))
# camera.start_preview()
camera.capture('image.jpg')

# allow the camera to warmup
time.sleep(0.1)

n=0
time = datetime.now()
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    # show the frame
    if(n>100):
        break
    n+=1

    # mem_image = image.flatten()
    print("B")
    # print(mem_image)

    cv2.imshow("Frame", image)
    # key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    # if key == ord("q"):
    # 	break
