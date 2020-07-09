# This is a testing py file handling mouse events in OpenCV.
# Brendan Ind 2020
# DWTFUL Licence (do what the **** you like)

import cv2 as cv
import numpy as np


# Create a program that paints a circle whenever/wherever we click with the mouse
# Firstly we create a mouse callback function which is executed whenever mouse clicked.
# This callback will return xy coords which we can use to plot a circle.

# To list all available events, run in shell:
def showEvents():
    events = [i for i in dir(cv) if 'EVENT' in i]
    print(events)
    # Returns something like: ['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', etc...]


# Code draws circle when double click:

# Mouse callback function
def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), 100, (255, 0, 0), -1)  # Create circle from mse xy points w/ r=100, green colour, pen=-1


# Create black canvas
img = np.zeros((512, 512, 3), np.uint8)  # Now img is a variable holding a greyish matrix.

# create normal window stuff
cv.namedWindow("image")  # We must name this window same as the one at the bottom in order for them to
# be the same window, otherwise we would have two windows, one displaying and other asking for mouse input.
cv.setMouseCallback('image', draw_circle)

# The setMouseCallback('window', function) is essentially like saying, in 'window' window, when there's ANY mouse action
# (be it double, single, click, etc..) then we will run the function
# (that is, the second argument in the setMouseCallback command) and its essentially pointing the program to the
# object of that function, like hey, there's been a mouse event, so program can you go run this function ere.
# We can then see in that circle function, we have particular parameters that the setMouseCallback gives us,
# so it automatically fills in the event, x, y, flags and param stuff. We might not need to use all of the information
# That the mouseCallback has given us, for example in the above example we only use the event, x and y, but its nice
# to know that we could also use flags, param, etc... (not sure what they nominally output but could find in docs).

# So now, our draw_circle() uses if statement to question weather the 'event' it received as a parameter from the
# mouseCallback() matches the one we are looking for (in this case its cv.EVENT_LBUTTONDBLCLK), then we act accordingly.


while True:
    cv.imshow('image', img)  # Where image is the window title (must be same as the title for cv.namedWindow() above
    # on line 32 and img is the matrix with that info in it.

    if cv.waitKey(20) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
