import numpy as np
import cv2


#Variable Assignment

k = cv2.waitKey(5) & 0xFF #For stopKeys
optionsArray = [np.zeros((300,512,3), np.uint8),"y","z"]
r=0
g=0
b=0



def choseFrame(bbox, sourceFrame):
    bbox = cv2.selectROI(sourceFrame,False)

def trackObject():
    print("Hello")

def initialiseTracking():
        print("Hello")


def initialiseMask():
    

def createTrackbars():
        print("Hello")


def createFrame(variable, source, option=False, options=optionsArray):
    if option == 0:
        variable = source #Make the inputted frame equal to the desired variable
    else:
        variable = options[option] # Else, use one of the options from the array
    
def showWindow(frame, label):
    cv2.imshow(label, frame)

def exitStrategy():
    if k == 27:
        cv2.destroyAllWindows()

    
