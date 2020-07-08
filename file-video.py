# This is a testing py file for dealing with videos from a saved file (charlie chaplain etc...), with opencv
# Brendan Ind 2020
# DWTFUL Licence (do what the **** you like)

# This is essentially the same as getting frmaes from a webcam but instead they're coming from a file not
# streamed from a device.

import numpy as np
import cv2 as cv

# Make variable of the file captured.
cap = cv.VideoCapture('vtest.avi')

while cap.isOpened(): # Ensures that while the video file is playing, do this. As soon as end, this loop breaks.
    ret, frame = cap.read()  # We take the two values returned from the read function that is done on the cap variable
    # It is comparable when we do word = "hello" then word.length(), we are performing an action on a matrix.

    # If frame correctly read, then ret = True hence:

    if not ret: # (i.e. if true, when ret = true)
        print("Couldn't read that frame, breaking")
        break

    # We are changing the matrix in the variable
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Now gray variable holds the matrix with all that photo data.
    print(grey)
