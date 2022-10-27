from multiprocessing.connection import Client
import cv2

address=('localhost',6000)
client=Client(address,authkey=b'secret password')
cap=cv2.VideoCapture(0)
while True :
    isTrue,frame=cap.read()
    if isTrue:
        client.send(frame)
client.close()
cap.close()