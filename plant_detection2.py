import cv2
from ultralytics import YOLO

#load a pretrained custom yolov8 model
model = YOLO("best.pt")

#export custom trained model and run live inference on webcam
results = model(source=0,show = True, conf = 0.7, save = False)