# Testing using trackbars to change colour palettes in cv2
# Brendan Ind 2020
# DWTFUL Licence (do what the **** you like)

# cv.createTrackbar takes args: 1) trackbar name 2) window name for which its attached (e.g. 'frame')
# 3) Default value its set to, 4) Max value possible 5) Callback function that happens when slider slides
# The callback function always has a default argument, which is the slider position.


import numpy as np
import cv2 as cv


# Here below is our callback function, except we dont actually need the reported value, so we just have a callback
# function (where x is the valaue of the slider) which does nothing witht aht information.
def nothing(x):
    pass


# Trackbars can also be used as on/off switches since cv2 doesnt actually have a button functionality.

# Create black matrix, like normal.
img = np.zeros((300, 512, 3), np.int8)
cv.namedWindow("image")

# Create trackbars for colour change
cv.createTrackbar("r", "image", 0, 255, nothing)
cv.createTrackbar("g", "image", 0, 255, nothing)
cv.createTrackbar("b", "image", 0, 255, nothing)

# Create on/off switch
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, "image", 0, 1, nothing)

# Main loop
while True:
    cv.imshow("image", img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:  # I.e. if esc key pressed
        break

    # Get current trackbar positions
    r = cv.getTrackbarPos('r', 'image')
    g = cv.getTrackbarPos('g', 'image')
    b = cv.getTrackbarPos('b', 'image')
    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:  # I.e. switch is off, dont change, make img just black.
        img[:] = 0  # Turn all values in the matrix to zero. (black)
    else:
        img[:] = [b, g, r]  # Change the relevant pixels to the colour values from the sliders.

# Cleanup
cv.destroyAllWindows()