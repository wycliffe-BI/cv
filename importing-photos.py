# Importing photos testing for cv2
# Brendan Ind 2020
# DWTFUL Licence (do what the **** you like)

import cv2 as cv
import sys
img = cv.imread(cv.samples.findFile("starry_night.jpg"))

if img is None:
    sys.exit("Couldn't read the image")

cv.imshow("Display window", img)

if k == ord("s"):
    cv.imwrite("starry_night.png", img)