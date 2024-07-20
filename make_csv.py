import pandas as pd
import datetime
import csv

path="D:\\Hack\\FACE_RECOGNITION PROJECT\\daily_attendance_csv_files"

currentdatetime=str(datetime.datetime.now()).split(" ")
datee=currentdatetime[0]

def make_csv_fn(csv_data):
    
        file_name=f"{path}\{datee}.csv"
        with open(file_name,mode='w',newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(csv_data)


