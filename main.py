## Brendan Ind NEA cv Tracking
## 2020-21
## DWTFUL Licence

import cv2
import numpy as np

def nothing(x):
    pass

def returnImg(x,y):
    # Return a black box of xy size
    print("Returning array of size "+str(x)+"x"+str(y))
    return np.zeroes((x,y,3), np.uint8)

def createTrackbar(label, frameName, min, max, changeFunction=nothing):
    print("Creating trackbar "+ label)
    cv2.createTrackbar(label, frameName, min, max, changeFunction)

def createTracker():
    print("Creating tracker")
    return cv2.trackerTLD_create()



class image

def __main__():
    print("Main running")
    cap = cap.VideoCapture(0)
    ROIunselected = True
    maskOff = False
    Print("Maskoff="+str(maskOff))
    print("ROIunselected="+ROIunselected)
    print("Entering mainloop")
    while (1):
        #take each frame