# pip install opencv-python==4.5.2
# import cv2
# # from controller import doorAutomate
# import time
# from database import *

# def front_camera():
    
#     video=cv2.VideoCapture(0)


#     facedetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#     recognizer = cv2.face.LBPHFaceRecognizer_create()
#     recognizer.read("Trainer.yml")

#     # imgBackground = cv2.imread("background.png")
#     personid=[]

# # def print_data(serial):
# #     if(serial != 'None'):
# #         get_data_by_face(serial)
#     while True:
     
#         serial=None
#         conf=0
#         ret,frame=video.read()
#         gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = facedetect.detectMultiScale(gray, 1.3, 5)
#         for (x,y,w,h) in faces:
#             serial, conf = recognizer.predict(gray[y:y+h, x:x+w])
#             # print(conf)
#             # print(serial)
#             if conf<50:
#                 cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
#                 cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
#                 cv2.rectangle(frame,(x,y-40),(x+w,y),(0,0,255),-1)
#             # cv2.putText(frame, (x, y-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
#             else:
#                 cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
#                 cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),2)
#                 cv2.rectangle(frame,(x,y-40),(x+w,y),(50,50,255),-1)
#             # cv2.putText(frame, (x, y-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
    
#         frame=cv2.resize(frame, (640, 480))
#         # imgBackground[162:162 + 480, 55:55 + 640] = frame
#         cv2.imshow("Frame",frame)
#         # print("hello")
#         if serial not in personid :
#             if conf < 60:
               
#         # personid.append(serial)
#                 personid.append(serial)
#         # get_data_by_face(serial)
#         # print_data(serial)
#                 if serial!=None:
               
#                     arrival_timeentry(serial)
#         k=cv2.waitKey(1)
    
#         if k==ord('o') and conf>50:
#         # doorAutomate(0)
#             time.sleep(10)
#         # doorAutomate(1)
#         if k==ord("q"):
#             break

#     print(personid)
# # leaving_timeentry(serial)
# # get_data_by_face(serial)
#     video.release()
#     cv2.destroyAllWindows()
# # front_camera()

#  back_camera()
import cv2
import time
from database import *

def initialize_camera(camera_index=0):
    video = cv2.VideoCapture(camera_index)
    if not video.isOpened():
        print("Error: Could not open camera.")
        return None
    return video

def load_models():
    facedetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("Trainer.yml")
    return facedetect, recognizer

def process_frame(frame, facedetect, recognizer, personid, conf_threshold=50):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    
    serial = None
    conf = 100  # Initialize with a high value to denote no face recognized
    
    for (x, y, w, h) in faces:
        serial, conf = recognizer.predict(gray[y:y+h, x:x+w])
        if conf < conf_threshold:
            color = (0, 255, 0)  # Green for Access Granted
            message = "Access Granted"
        else:
            color = (0, 0, 255)  # Red for Access Denied
            message = "Access Denied"
        
        # Draw rectangles and text
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.rectangle(frame, (x, y - 40), (x + w, y), color, -1)
        cv2.putText(frame, message, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        if serial not in personid and conf < 80:
            personid.append(serial)
            if serial is not None:
                arrival_timeentry(serial)
    return frame, serial, conf

def front_camera():
    video = initialize_camera()
    if video is None:
        return

    facedetect, recognizer = load_models()
    personid = []

    while True:
        ret, frame = video.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        frame, serial, conf = process_frame(frame, facedetect, recognizer, personid)
        frame = cv2.resize(frame, (640, 480))
        cv2.imshow("Frame", frame)

        k = cv2.waitKey(1)
        if k == ord('o') and conf > 50:
            time.sleep(10)
        if k == ord("q"):
            break

    video.release()
    cv2.destroyAllWindows()
