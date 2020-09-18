##import numpy as np
##import cv2
##
##cap = cv2.VideoCapture(0)
##
##
##
##def nothing(x):
##        pass
##
##
##while(True):
##    # Capture frame-by-frame
##    ret, frame = cap.read()
##    cv2.createTrackbar('H','frame',0,255,nothing)
##    cv2.createTrackbar('S','frame',0,255,nothing)
##    cv2.createTrackbar('V','frame',0,255,nothing)
##    # Our operations on the frame come here
##    colourFilter = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #COLOR_BGR2HSV
##
##    # Display the resulting frame
##    cv2.imshow('frame',frame) #replace the sconf frame with colourFilter to apply the colour filters
##    if cv2.waitKey(1) & 0xFF == ord('q'):
##        break
##
## ##When everything done, release the capture
##cap.release()
##cv2.destroyAllWindows()
##



import cv2
import numpy as np

cap = cv2.VideoCapture(0)


r=0
g=0
b=0

lower_blue = np.array([r,g,b])
upper_blue = np.array([r+80,g+80,b+80])

def nothing(x):
    pass

img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('frame')


cv2.createTrackbar('r','frame',0,255,nothing)
cv2.createTrackbar('g','frame',0,255,nothing)
cv2.createTrackbar('b','frame',0,255,nothing)
cv2.createTrackbar('s','frame',0,1,nothing)

##create tracker

print("Creating Tracker")

tracker = cv2.TrackerTLD_create()  ##TrackerKCF_create()

print("Tracker Created")


#set ROI unselected
ROIUnselected = True


maskOff = False

print("ROI and MaskOff Vars set, going into main loop")



while(1):
    
    # Take each frame

    

    _, frame = cap.read()
    


    s = cv2.getTrackbarPos('s','frame')


    if s == 0:
        maskOff = True
    else:
        maskOff = False

    

    r = cv2.getTrackbarPos('b','frame')
    g = cv2.getTrackbarPos('g','frame')
    b = cv2.getTrackbarPos('r','frame')

    lower = np.array([r,g,b])
    upper = np.array([r+100,g+100,b+100])
    
    # Convert BGR to HSV
    ##rgb = frame ##cv2.cvtColor(frame, cv2.COLOR_BGR) ##  BGR2HSV

    # define range of blue color in HSV
    

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(frame, lower, upper)  ##lower, upper

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    if maskOff == True:
        res = frame
    else:
        res = res

        
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

    if ROIUnselected == True:

        bbox = cv2.selectROI(res, False)
        
        ok = tracker.init(res, bbox)

        ROIUnselected = False

    

    ##do tracking on the res frame

    


    #UPDATE THE TRACKERS

    ok, bbox = tracker.update(res)
    
    if ok:
        # Tracking success
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
    else :
        # Tracking failure
        cv2.putText(res, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
    

cv2.destroyAllWindows()


##





##import cv2
##import numpy as np
##
##def nothing(x):
##    pass
##
### Create a black image, a window
##img = np.zeros((300,512,3), np.uint8)
##cv2.namedWindow('image')
##
### create trackbars for color change
##cv2.createTrackbar('R','image',0,255,nothing)
##cv2.createTrackbar('G','image',0,255,nothing)
##cv2.createTrackbar('B','image',0,255,nothing)
##
### create switch for ON/OFF functionality
##switch = '0 : OFF \n1 : ON'
##cv2.createTrackbar(switch, 'image',0,1,nothing)
##
##while(1):
##    cv2.imshow('image',img)
##    k = cv2.waitKey(1) & 0xFF
##    if k == 27:
##        break
##
##    # get current positions of four trackbars
##    r = cv2.getTrackbarPos('R','image')
##    g = cv2.getTrackbarPos('G','image')
##    b = cv2.getTrackbarPos('B','image')
##    s = cv2.getTrackbarPos(switch,'image')
##
##    if s == 0:
##        img[:] = 0
##    else:
##        img[:] = [b,g,r]
##
##cv2.destroyAllWindows()




####COLOUR PICER UNEDITED BELOW:
##import cv2
##import numpy as np
##
##def nothing(x):
##    pass
##
### Create a black image, a window
##img = np.zeros((300,512,3), np.uint8)
##cv2.namedWindow('image')
##
### create trackbars for color change
##cv2.createTrackbar('R','image',0,255,nothing)
##cv2.createTrackbar('G','image',0,255,nothing)
##cv2.createTrackbar('B','image',0,255,nothing)
##
### create switch for ON/OFF functionality
##switch = '0 : OFF \n1 : ON'
##cv2.createTrackbar(switch, 'image',0,1,nothing)
##
##while(1):
##    cv2.imshow('image',img)
##    k = cv2.waitKey(1) & 0xFF
##    if k == 27:
##        break
##
##    # get current positions of four trackbars
##    r = cv2.getTrackbarPos('R','image')
##    g = cv2.getTrackbarPos('G','image')
##    b = cv2.getTrackbarPos('B','image')
##    s = cv2.getTrackbarPos(switch,'image')
##
##    if s == 0:
##        img[:] = 0
##    else:
##        img[:] = [b,g,r]
##
##cv2.destroyAllWindows()
