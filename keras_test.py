## Brendan Ind
## DWTFUL

from keras import load_model
import numpy as np
import cv2

model = load_model(path)  # Open saved model from the path that the project is in.


def predict_image(image):
    image = np.array(image, dtype="Float32")
    image /= 255
    pred_array = model.predict(image)

    print(pred_array)

    # model.predict() returns an array of possibilities that it could be.
    # np.argmax grabs the index of the highest probability

    result = gesture_names[np.argmax(pred_array)]

    ## Score is float, we want it to 2dp
    score = float("%0.2f" % (max(pred_array[0]) * 100))  #

    ## Print and return all the information
    print(f'RESULT: {result}, SCORE,: {Score}')
    return result, score


camera = cv2.VideoCapture(0)

while camera.isOpened():
    # Return True if the camera is on and working, otherwise never run this loop.
    ret, frame = camera.read()

    k = cv2.waitKey(10)

    if k == 32: #If spacebar is pressed, we take frame and do prediction on it.
        frame = np.stack((frame,)*3, axis=1)
        frame = cv2.resize(frame, (224,224,3))
        frame = frame.reshape(1, 224, 224, 3)
        prediction, score = predict_image(frame)