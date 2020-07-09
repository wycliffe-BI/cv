# This is a testing py file handling mouse events in OpenCV, a more complicated version
# Brendan Ind 2020
# DWTFUL Licence (do what the **** you like)

import numpy as np
import cv2 as cv

drawing = False  # True if mouse pressed
mode = True  # If True, draw a  rectangle, Press 'm' to toggle to curve.

ix, iy = -1, -1


# Mouse callback function:

def callbackMouse(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv.circle(img, (x, y), 5, (0, 0, 255), -1)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            cv.circle(img, (x, y), 5, (0, 0, 255), -1)


# Make matrix variable
img = np.zeros((512, 512, 3), np.uint8)

cv.namedWindow("window")
cv.setMouseCallback("window", callbackMouse)  # Essentially runs callbackMouse when there's any mouse event.

while True:
    cv.imshow("window", img)
    k = cv.waitKey(1) & 0xFF
    if k == ord("m"):
        mode = not mode # Switch em back around
    elif k == 27: # chr(27) = ESC key
        break # Break if ESC button pressed.

cv.destroyAllWindows()