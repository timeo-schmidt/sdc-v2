import cameraController as cc
import os

from pympler.tracker import SummaryTracker
tracker = SummaryTracker()

try:
    os.system("sudo modprobe bcm2835-v4l2")
    cc.setupCamera()
    #Infinitely Record Frames until Interrupt
    cc.recordTrainingData()
except KeyboardInterrupt:
    print("")
    print("")
    print("")
    print("")
    tracker.print_diff()
    print("")
    print("")
    print("")
    print("")
    print("")
