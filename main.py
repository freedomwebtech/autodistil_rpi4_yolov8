import cv2
from ultralytics import YOLO
import pandas as pd
import cvzone


model = YOLO()  



cap=cv2.VideoCapture('forklift.mp4')
my_file = open("coco1.txt", "r")
data = my_file.read()
class_list = data.split("\n")



count=0
while True:
    ret,frame = cap.read()
    count += 1
    if count % 3 != 0:
        continue
    if not ret:
       break
    frame = cv2.resize(frame, (1020, 600))

    results = model(frame,imgsz=240)
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")
    list=[]
    for index, row in px.iterrows():
        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])
        
        d = int(row[5])
        c = class_list[d]
        
        if "forklift" in c:
            cvzone.putTextRect(frame,f'{c}',(x1,y1),1,1)
            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
        elif "person" in c:
        cvzone.putTextRect(frame,f'{c}',(x1,y1),1,1)
        cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)
            

    
    
    cv2.imshow("FRAME", frame)
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
