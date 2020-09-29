# This is a testing py file for dealing with videos from a camera (webcam, etc..) with opencv
# Brendan Ind 2020
# DWTFUL Licence (do what the **** you like)

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannooot find a camera mate")
    exit()

while True:
    # Capture video frame by frame
    # Where the return of cap.read() is twofold, first being boolean telling if the capture of frame was success, and
    # Other is the matrix that has actually got the color data from that frame.
    ret, frame = cap.read()

    # If frame read correctly
    if not ret: #The not of FALSE is true, hence when the cap.read() returns false, this code will run.
        print("Can't receive frame")
        break

    # We then to some cool shii with each frame here: (colour editing n stuff)
    # We make a new matrix (frame) that is a grey tinted version of the "frame" variable that we got from the capture()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GREY) # New variable with greyed matrix

    # Display the captured frames as if they're a single frame, like in the image .py file
    cv.imshow("frame", grey) #Where 'frame' corresponds to the window heading and grey is the variable w/ matrix to show.
    if cv.waitKey(1) == ord('q'):
        break

# Out of loop, when all the capture is done, or q is pressed:

cap.release()
cv.destroyAllWindows()

# We can also access other parts of the incoming capture with:
# cap.get(cv.CAP_PROP_FRAME_WIDTH) and cap.get(cv.CAP_PROP_FRAME_HEIGHT)
# cap.set(cv.CAP_PROP_FRAME_WIDTH, 320) to set it.
