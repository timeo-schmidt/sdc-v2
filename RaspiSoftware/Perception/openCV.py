import numpy as np
import cv2
import time


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320) #CV_CAP_PROP_FRAME_WIDTH
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240) #CV_CAP_PROP_FRAME_HEIGHT
cap.set(cv2.CAP_PROP_FPS, 100) #CV_CAP_PROP_FPS
n = 0
startTime = time.time()
while(n<500):
    n+=1
    # Capture frame-by-frame
    _, frame = cap.read()

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(str(n/(time.time()-startTime)) + "FPS")

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
