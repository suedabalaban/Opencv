import cv2
from ultralytics import YOLO

cap = cv2.VideoCapture(0)
model = YOLO("best.pt")

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)

    result = model(frame)

    cv2.imshow("frame", frame)

    if cv2.waitkey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()