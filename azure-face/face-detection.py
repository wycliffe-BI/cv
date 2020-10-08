## Brendan Ind
## Azure face detection

import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, \
    OperationStatusType


def detectFace(face_client, image_url):
    '''
    :param face_client:
    This is the face_client which is --> face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))
    so that goes in here.

    :param image_url:
    This is the url of the image that we want to analyse.
    https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AAzOjos.img?h=630&w=1200&m=6&q=60&o=t&l=f&f=jpg&x=1542&y=820

    :return:
    This will return the object that contains all the data about that photo that we just analysed.
    '''

    # Set the name of the image as its path
    image_name = os.path.basename(image_url)

    # Object of detected faces is equal to the azure face client algorithm
    detected_faces = face_client.face.detect_with_url(url=image_url, True, True, null)
    # .detect_with_url can take an extra arg, detectionModel="detection_02"

    # If we dont detect faces then we return nothing and raise an error
    if not detected_faces:
        raise Exception('No face detected from image {}'.format(image_name))

    # Print our results!
    print('Detected face ID from', image_name, ':')
    for face in detected_faces:
        print(face.face_id)

    # Return an object (dictionary) of all the faces and their relevant information.
    return detected_faces


def getRectangle(detectedFacesDictionary):
    '''

    :arg detectedFacesDictionary is the dictionary that detectFace spits out
    that has all the relevant information regarding the url picture.

    '''

    rect = detectedFacesDictionary.face_rectangle
    left = rect.left
    top = rect.top
    right = left + rect.width
    bottom = top + rect.height

    return ((left, top), (right, bottom))


def downloadPhoto(imageURL):
    response = requests.get(imageURL)
    img = Image.open(BytesIO(response.content))

    # Return that bit representation of that downloaded url image
    return img


def drawRect(img, detectedFacesDict):
    '''
    :param img is the return of the downloadPhoto() function and is a byte representation of the url photo.

    :param detectedFacesDict is that dictionary that the initial azure cloud returned
    '''

    print('Drawing rectangle around face... see popup for results.')
    draw = ImageDraw.Draw(img)

    # For each element in the dictionary that the azure returned, we draw the rectangle, getting the measurements
    # from that function getRectangle() form earlier.
    for face in detectedFacesDict:
        draw.rectangle(getRectangle(face), outline='red')

    #Return an image with the boxes on them
    return img


## START OF ACTUAL CODE

## Set the keys for accessing azure cloud applications, set these on CONTROL PANEL on local machine, see readme for more.
## TODO: Add to the readme to explain how the tokens work and global variables and stuff.
KEY = os.environ['FACE_SUBSCRIPTION_KEY']
ENDPOINT = os.environ['FACE_ENDPOINT']

# Create an authenticated FaceClient.
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

face_url = 'https://www.whitehouse.gov/wp-content/uploads/2017/11/President-Trump-Official-Portrait-1024x1297.jpg'

dictionaryOfFaces = detectFace(face_client, face_url)

face_img = downloadPhoto(face_url)

img = drawRect(face_img, dictionaryOfFaces)

img.show()


for face in dictionaryOfFaces:
    print(face)


print("Face rect " + str(dictionaryOfFaces.face_rectangle))
print("Face landmarks "+ str(dictionaryOfFaces.face_landmarks))
print("Face attributes "+ str(dictionaryOfFaces.face_attributes))