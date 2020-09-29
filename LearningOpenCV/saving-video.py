# Testing saving videos in cv2.
# Brendan Ind 2020
# DWTFUL Licence (do what the **** you like)

# With images, if we wanted to save them, we would use cv.imwrite("name.png", matrix), but with videos its a bit harder.
# We create a VideoWriter object then a ton of args: filename, FourCC code, fps, frame size, isColor flag (True, False)

# FourCC is a 4-byte code used to specify the video codec, list of available codes can be found at fourcc.org
# In windows we mainly use DIVX cos it says it works best, I'm not gonna question it.


import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')  # This could also be DIVX
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # This is in the order VideoWriter(filename,
# fourccVariableDefinedAbove, fps, resolutionAsList)

if not cap.isOpened():
    print("No capture device")

while cap.isOpened():
    ret, frame = cap.read()  # Where cap was defined earlier as the video capture device hardware.
    if not ret:
        print("Couldn't fetch that frame soz")
        break
    frame = cv.flip(frame, 0)  # This is an additional step that literally just mirrors the image and replaces the
    # variable with itself, similar to x = x+1 except we a re doing a transformation on the matrix

    # Write out the flipped frame to the fourcc object
    out.write(frame)  # out is the variable which is the cc video writer object, so we are using that object and
    # giving it an argument (the current frame) and it will string it together each frame

    cv.imshow('frame', frame)  # Where we then show the frame variable

    if cv.waitKey(1) == ord("q"):
        break

# Release everything outside of loop when the file is complete
cap.release()
out.release()  # Where out is the videoWriter object containing all the stitched frames
cv.destroyAllWindows()