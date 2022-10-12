from pickletools import uint8
import numpy as np
import cv2 
import math

points = np.zeros((4,2),np.int)
count = 0 
def mousePoints(event,x,y,flag,params):
    global count 
    if event == cv2.EVENT_LBUTTONDOWN :
      points[count] = x,y
      print(x,y)
      count +=1
img = cv2.imread('task_5/johnsmith.jpg')
clone = img.copy()
while(True):
    if count == 4 :
        width = int(math.sqrt( pow((points[1][0] - points[0][0]),2) + pow((points[1][1] - points[0][1]),2)))
        height = int(math.sqrt( pow((points[3][0] - points[0][0]),2) + pow((points[3][1] - points[0][1]),2) ))
        pt1 = np.float32([points[0],points[1],points[2],points[3]])
        pt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        # print (width)
        # print(height)
        mat = cv2.getPerspectiveTransform(pt1,pt2)
        imgOutput = cv2.warpPerspective(clone,mat,(width,height))
        cv2.imshow("Output image",imgOutput)
    for i in range(0,4) :
        cv2.circle(img,(points[i][0],points[i][1]),10,(255,0,0),cv2.FILLED)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', mousePoints)
    cv2.imshow('image', img)
    k=cv2.waitKey(1) & 0xFF
    if k==27: 
        break
    cv2.waitKey(1)
