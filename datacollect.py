# pip install opencv-python==4.5.2
from database import *
def iamgetaker(id,fname,lname,address,wh_no,email):
    import cv2 
    import random

    video=cv2.VideoCapture(0)
    facedetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    # print(id,fname,lname,address,wh_no,email)
    # id=int(input("Id:"))
    # fname=input("Fname:")
    # lname=input("Lname:")
    # address=input("Address:")
    # wh_no=int(input("Whatsapp No:"))
    # email=input("Email:")
    # id = int(id)
    # wh_no=int(wh_no)
    add_record(id,fname,lname,address,wh_no,email,)
    emp_timing(id)
    count=0

    while True:
        ret,frame=video.read()
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = facedetect.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            count=count+1
            cv2.imwrite('datasets/User.'+str(id)+"."+str(count)+".jpg", gray[y:y+h, x:x+w])
            cv2.rectangle(frame, (x,y), (x+w, y+h), (50,50,255), 1)

        cv2.imshow("Frame",frame)

        k=cv2.waitKey(1)

        if count>500:
            break

    video.release()
    cv2.destroyAllWindows()
    print("Dataset Collection Done..................")

# iamgetaker()