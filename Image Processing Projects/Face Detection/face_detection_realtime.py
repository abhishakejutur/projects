import cv2
import numpy as np

face_detector1 = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_dectector1 = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


# reading the input image now
cap = cv2.VideoCapture(1)

while cap.isOpened():
    _, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector1.detectMultiScale(gray,1.1, 4 )
    
    for (x,y, w, h) in faces:
        cv2.rectangle(frame, pt1 = (x,y),pt2 = (x+w, y+h), color = (255,0,0),thickness =2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_dectector1.detectMultiScale(roi_gray)
    
        for (ex,ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)

        cv2.imshow("window", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
frame.release()
