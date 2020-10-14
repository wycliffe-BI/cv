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


class Photo:
    def __init__(self, location, url, client):
        '''
                --> attributes:: is a list of the things that we want to return, usually ["emotion"]

                --> location:: is the location (local or url) of the photo

                --> url:: is a bool that is set to true default if the location that you set is a URL,
                          if its a local location then set to false so that it can be dealt with accordingly.

                --> faceclient:: is the obejct: FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))
                                 Set as default as face_client, since that's what it will be usually.
                '''

        self.location = location
        self.url = url
        self.client = client

    def download(self):
        if self.url:  ## Make sure we are dealing witha  url photo, not local
            response = requests.get(self.location)
            img = Image.open.(BytesIO(response.content))
            return img

    def findFace(self):  ## url, location, attributes

        if self.url == True:  ## I.e. its a webimage.
            ## Set the image name to its pathname
            image_name = os.path.basename(self.location)

            ## Return the object with all the faces in it.
            detected_faces = face_client.face_detect_with_url(url=location, return_face_attributes=attributes)
            return detected_faces

        else:
            print("Local file, not done yet")
            ## TODO: Get local files done!


class Face:
    def __init__(self, id, emotions, coords):
        self.id = id
        self.emotions = emotions
        self.coords = coords

    ##def url(self):

    def emotions(self):
        print("return the azure emotions of ")


def detectFace(face_client, image_url, attributesToReturn):
    '''
    :param face_client:
    This is the face_client which is --> face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))
    so that goes in here.

    :param image_url:
    This is the url of the image that we want to analyse.
    https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AAzOjos.img?h=630&w=1200&m=6&q=60&o=t&l=f&f=jpg&x=1542&y=820

    ;param attributesToReturn:
    this is a list of the things that the azure API will respond with, for example ["emotion"] will respond with the

    :return:
    This will return the object that contains all the data about that photo that we just analysed.
    '''

    # Set the name of the image as its path
    image_name = os.path.basename(image_url)

    # Object of detected faces is equal to the azure face client algorithm
    detected_faces = face_client.face.detect_with_url(url=image_url, return_face_attributes=attributesToReturn, )

    # .detect_with_url can take args that can be found at:
    # https://docs.microsoft.com/en-us/python/api/azure-cognitiveservices-vision-face/azure.cognitiveservices.vision.face.operations.faceoperations?view=azure-python#detect-with-url-url--return-face-id-true--return-face-landmarks-false--return-face-attributes-none--recognition-model--recognition-01---return-recognition-model-false--detection-model--detection-01---custom-headers-none--raw-false----operation-config-

    # If we dont detect faces then we return nothing and raise an error
    if not detected_faces:
        raise Exception('No face detected from image {}'.format(image_name))

    # Print our results!
    print('Detected face ID from', image_name, ':')
    for face in detected_faces:
        print(face.face_id)

    # Return an object (dictionary) of all the faces and their relevant information.
    return detected_faces


##def detectEmotion(faceDict, emotionsToDetect):


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

    # Return an image with the boxes on them
    return img


def getEmotion(detectedFacesDictionary):
    emotions = detectedFacesDictionary.emotion()
    return emotions


## START OF ACTUAL CODE

faceAttributes = ["emotion"]

## Set the keys for accessing azure cloud applications, set these on CONTROL PANEL on local machine, see readme for more.
## TODO: Add to the readme to explain how the tokens work and global variables and stuff.
KEY = os.environ['FACE_SUBSCRIPTION_KEY']
ENDPOINT = os.environ['FACE_ENDPOINT']

# Create an authenticated FaceClient.
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

face_url = 'https://upload.wikimedia.org/wikipedia/commons/5/55/Dalailama1_20121014_4639.jpg'

dictionaryOfFaces = detectFace(face_client, face_url, faceAttributes)

face_img = downloadPhoto(face_url)

img = drawRect(face_img, dictionaryOfFaces)

img.show()

for face in dictionaryOfFaces:
    emotionObject = face.face_attributes.emotion
    print(face)
    print(emotionObject)
