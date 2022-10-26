import cv2 
import numpy as np

img = cv2.imread('task_6/OneYearImage.jpg')
image2 = cv2.imread('task_6/Coral1.jpg')
mask = img.copy()
clone = image2.copy()
image = np.zeros((680,840,3),np.uint8)
image[:] = 0,0,0
image[0:(0+mask.shape[0]), 100:(100+mask.shape[1])] = mask
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

n1=0
n2=0
cog=[]
cob=[]
def mousePoints(event,x,y,flag,params):
    if (event == cv2.EVENT_LBUTTONDOWN)  :
        print(x,y)
        L(x,y)
    elif (event == cv2.EVENT_RBUTTONDOWN) :
        R(x,y)

def L(x,y) :
    global image2,n1,n2,cog,cob
    if  (n1 < 2) :
        if n1 == 0 :
            cog.clear()
        n1 += 1 
        cog.append((x,y))
        print(cog)
    if n1 == 2 :
        cv2.rectangle(image2,(cog[0]),(cog[1]),(255, 0, 0),2)
        cog.clear()
        n1 = 0
def R(x,y) :
    global image2,n1,n2,cog,cob
    if  (n2 < 2) :
        if n2 == 0 :
            cob.clear()
        n2 += 1 
        cob.append((x,y))
        print(cob)
    if n2 == 2 :
        cv2.rectangle(image2,(cob[0]),(cob[1]),(0, 255, 0),2)
        cob.clear()
        n2 = 0
def AddText(img) :
        cv2.putText(img, text='Left click to add a green rectangle', org=(655, 355), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=0.7, color=(0, 255, 0),thickness=1)
        cv2.putText(img, text='Right click to add a blue rectangle', org=(655, 385), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=0.7, color=(0, 255, 0),thickness=1)
        cv2.putText(img, text='Press "d" to clear', org=(655, 415), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=0.7, color=(0, 255, 0),thickness=1)
        cv2.putText(img, text='Press "q" to exit', org=(655, 445), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=0.7, color=(0, 255, 0),thickness=1)
while True :
    stacked = stackImages(1,[image2,image])
    AddText(stacked)
    cv2.imshow('RES',stacked)
    cv2.setMouseCallback('RES', mousePoints)
    k=cv2.waitKey(1) & 0xFF
    if k==100:
        image2 = clone.copy()
    if k==113: 
        break
cv2.waitKey(0)
