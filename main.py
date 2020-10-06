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

def sliderPos(name, frame):
    return cv2.getTrackbarPos(name, frame)

def createTracker():
    print("Creating tracker")
    return cv2.trackerTLD_create()

def bgr_to_hsv(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR)

def bitwiseCombine(frame, mask):
    """
    combines the current frame (arg1) with another mask
    frame (arg2) to combine them together and
    returns the new frame, which you should save as a
    variable e.g. res frame.
    """
    return cv2.bitwise_and(frame, frame, mask)

##class image

def __main__():
    print("Main running")
    cap = cap.VideoCapture(0)
    ROIunselected = True
    maskOff = False
    Print("Maskoff="+str(maskOff))
    print("ROIunselected="+ROIunselected)
    print("Entering mainloop")
    while (1):
        # Take each frame
        _, frame = cap.read()