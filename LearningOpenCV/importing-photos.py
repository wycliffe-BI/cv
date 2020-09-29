# Importing photos testing for cv2
# Brendan Ind 2020
# DWTFUL Licence (do what the **** you like)

# Import stuff
import cv2 as cv
import sys

# img is essentially a big matrix, woooow
img = cv.imread("starry_night.jpg")

if img is None:  # i.e. no image
    sys.exit("Couldn't read the image")

cv.imshow("Display window", img)
k = cv.waitKey(0)  # parameter is how long program should wait for user input (in this case 0 is forever)

if k == ord("s"):
    cv.imwrite("starry_night.png", img)  # This writes the file back to the dir, i.e. it will arrive in .png format in
    # the directory of this project ,,,,, WHERE img second arg is the matrix of data.
