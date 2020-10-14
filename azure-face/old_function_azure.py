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

def getRectangle(singleFaceFromDict):
    '''

    :arg detectedFacesDictionary is the dictionary that detectFace spits out
    that has all the relevant information regarding the url picture.

    '''

    rect = singleFaceFromDict.face_rectangle
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

