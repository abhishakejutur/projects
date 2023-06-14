import cv2
import numpy as np

face_detector1 = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_dectector1 = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cap=cv2.VideoCapture(0)

while(1):
    res,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_detector1.detectMultiScale(gray)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        

    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
