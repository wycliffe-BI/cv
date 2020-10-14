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
    def __init__(self, location, url, client, attributes):
        """
        :param location: url/physical place where the photo is
        :param url: bool to say if its a url or local (url=True if so)
        :param client: is object: FaceClient(ENDPOINT, Cog.......)
        :param attributes: list of things that are returned, usually ["emotions"]
        """

        self.location = location
        self.url = url
        self.client = client
        self.attributes = attributes

    def download(self):
        if self.url:  ## Make sure we are dealing witha  url photo, not local
            response = requests.get(self.location)
            img = Image.open(BytesIO(response.content))
            return img

    def faces(self):
        if self.url:  ## I.e. it's a web image. (True)
            ## Set the image name to its pathname
            image_name = os.path.basename(self.location)

            ## Get object with all the faces in it
            detected_faces = face_client.face.detect_with_url(url=self.location, return_face_attributes=self.attributes)
            if not detected_faces: # None found, returns False:
                raise Exception("Cannot find any faces in the photo!")

            ## Print results to console
            for i in detected_faces:
                print(i)

            ## Return that object back to the main section
            return detected_faces
        else:  ##I.e. local images.
            print("Local file, not done yet")
            ## TODO: Get local files done!

class Face:
    def __init__(self, singleFace, tag, emotionsList, coords):
        self.singleFace = singleFace
        self.tag = tag
        self.emotionsList = emotionsList
        self.coords = coords

    def emotionValue(self, emotion="none"):
        if emotion == "none":
            print("Didn't get the arg I wanted to return an emotion")
        emotions = self.singleFace.face_attributes
        print("These are the emotions it returned from that face:")
        print(emotions)
        ## TODO: parse the emotions object to return required emotion.

class Box:
    def __init__(self, image, face):
        self.image = image
        self.face = face

    def get(self):
        rect = self.face.face_rectangle
        left = rect.left
        top = rect.top
        right = left + rect.width
        bottom = top + rect.height

        ## All the information we need ot build a rectangle:
        info = ((left, top), (right, bottom))

        return info

    def draw(self, info, img):

        ## Record that onto the photo:
        draw = ImageDraw.Draw(img)
        draw.rectangle(info, oultine="red")

        return img





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
