import cv2
from ultralytics import YOLO

import cvzone
import math

cap = cv2.VideoCapture(0)

model = YOLO("best.pt")

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)

    results = model(frame)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1),int(x2),int(y2) #casting

            w, h = x2-x1,y2-y1 #adjusting weight and height of boxes

            cvzone.cornerRect(frame,(x1,y1,w,h))

            conf = math.ceil((box.conf[0]*100))/100

            cls = box.cls[0]


    cv2.imshow("frame", frame)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

