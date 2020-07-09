# This is a testing py file for doing geometry in opencv, drawing lines.
# Brendan Ind 2020
# DWTFUL Licence (do what the **** you like)

import cv2 as cv
import numpy as np

# Create  a black canvas image
img = np.zeros((512, 512, 3), np.uint8)  # Make a friggin huge matrix with black pixels. (512x512)

# Draw a diagonal blue line with thickness of 5 px:
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)  # Args are as follows:
# cv.Line(img(canvas), point1, point2, color(in bgr?), thickness=1, lineType=8, shift=0) → returns nothing

# Draw a rectangle
cv.rectangle(img, (380, 0), (510, 128), (0, 255, 0), 3)
# I.e. rect(img canvas, two points, gbr makes green, and line thick = 3)

cv.circle(img, (447, 63), 63, (0, 0, 255), -1)
# Just made a circle with canvas=img, centre (447,63), radius 63, color red (0,0,255), and line thic -1

cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, (255), -1)
# Make ellipse with canvas=img, centre, axis, angle, startAngle, endAngle, color, thickness, bunch of other deflt vals.)

# Define some points in an array to use to draw a polyline:
pts = np.array([[10,5], [20,30], [70,20], [50,10]], np.int32)
# Where np.array(object, dtype (usually np.int32))
# Where object is a 2D array, elg.== [[10,10], [5,5]]

# Draw polyline
cv.polylines(img, [pts], True, (0, 255, 255))  # canvas=img, points array, isClosed=True, color=red+blue (purple)

# Draw some text
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, "OpenCV", (10, 500), font, 4, (255,255,255), 2, cv.LINE_AA)
# Where the args are: cv.putText(canvas=img, "String to display", position (bottom leftmost), font(defined earlier),
# font scale, colour (255, 255, 255) is white, thickness (2), linetype,e.g(cv.LINE_AA))

cv.imshow('window name', img)  # In the form imshow(name(str), matrix)

k = cv.waitKey(0)  # To stop window closing straight away