import datetime as dt
import cv2
import numpy as np
import os
import pickle
import drivingController as dc
import time



printDebug = True

def setupCamera(resolutionArray=[640,480], frameRateSetting=90):
    global camera
    # To enable raspicam, install drivers -->  sudo modprobe bcm2835-v4l2
    camera = cv2.VideoCapture(0)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, resolutionArray[0])
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, resolutionArray[1])
    camera.set(cv2.CAP_PROP_FPS, frameRateSetting)

# Training Data is stored as dumped pickle arrays
def recordTrainingData(saveLocationPath="trainingData/", bw=False, displayOnScreen=False, numberOfFrames=-1):
    # numberOfFrames: -1 [infinite recording]

    if(not camera):
        print("[cameraController] Init Camera First")
        return
    print("[cameraController] Training Data Collection Started")

    storagePath = saveLocationPath + str(dt.datetime.now()) + "/"
    os.makedirs(storagePath)

    fidx = 0

    recordStartingTime = dt.datetime.utcnow().timestamp()
    while(numberOfFrames==-1 or fidx<=numberOfFrames):

        if(printDebug):
            print(time.time())

        _, frameArray = camera.read()

        # Display Recording Camera On Screen
        if(displayOnScreen):
            # Significantly Reduces Framerate, Demo+Debug Purposes
            dotBlinkRed = int((dt.datetime.now().microsecond/1000000*255))
            displayIMG = cv2.circle(frameArray, (20,20), 10, (0,0,dotBlinkRed),-10)
            displayIMG = cv2.putText(displayIMG, "Frames Recorded:" + str(fidx), (50, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
            displayIMG = cv2.putText(displayIMG, "Black&White:" + str(bw), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
            cv2.imshow('Training Data Collection', displayIMG)
            if cv2.waitKey(1) == 27:
    	           break  # esc to quit

        # Convert Frame To Black and White
        if(bw):
            frameArray = cv2.cvtColor(frameArray, cv2.COLOR_BGR2GRAY)


        # DumpArrayToDisk
        frameArray = np.array(frameArray).flatten()
        pickle.dump(frameArray, open(storagePath + str(fidx),"wb") )

        fidx += 1

    timeDiff = dt.datetime.utcnow().timestamp()-recordStartingTime
    averageFPS = float(fidx)/(dt.datetime.utcnow().timestamp()-recordStartingTime)

    cv2.destroyAllWindows()
    print("[cameraController] Average Recording Framerate: " + str(averageFPS) + "FPS")
    print("[cameraController] Training Data Collection Finished")
    return True, numberOfFrames

def createVideoSample(duration):
    vidWriter = cv2.VideoWriter_fourcc(*'FMP4')
    out = cv2.VideoWriter('sample.mp4',vidWriter, 30.0, (640,480))
    startingTime = dt.datetime.utcnow().timestamp()
    while((dt.datetime.utcnow().timestamp()) < startingTime + duration):
        _, frame = camera.read()
        out.write(frame)
    out.release()
