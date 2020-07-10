# This is a testing py file for basic operations on images with openCV
# Brendan Ind 2020
# DWTFUL Licence (do what the **** you like)

# Learn to:
# - Access pixel values and modify them
# - Access image properties
# - Set a region of interest (ROI)
# - Split and merge images

# (a lot of these operations are numpy stuff, manipulating matrices)

import numpy as np
import cv2 as cv
from time import sleep

# Load a colour image:
img = cv.imread('messi5.jpg')


def row_by_row(img=img):
    # We can access a pixel value by its row and column coordinates
    px = img[100, 100]
    print(px)
    print("Returned [157, 166, 200]?")


def only_blue(img=img):
    # Access only the blue pixels
    blue = img[100, 100, 0]  # bgr
    print(blue)
    print("returned 157?")


def modify_pixels(img=img):
    img[100, 100] = [255, 255, 255]
    print(img[100, 100])
    print("Should return [255, 255, 255]")


print("Size of image:")
print(img.size)
sleep(1)

print("dtype is: (uint8 hopefully...)")
print(img.dtype)
sleep(1)

# What we could do is cut a ROI (region of interest) and use matrix transformations to move it in the image.
# Say our image of mess has the ball at:

ball = img[280:340, 330:390]  # ball is in this region

# then let:
img[273:333, 100:160] = ball  # Replace pixels in the new region with the ball pixels

cv.imshow("Display window", img)

k = cv.waitKey(0)  # parameter is how long program should wait for user input (in this case 0 is forever)
