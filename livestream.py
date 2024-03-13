#livestream to jetson nano
import cv2

cap = cv2.VideoCapture(0)

#define mjpeg codec
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480)) #VideoWriter initializes a video writer object to save the frames to a file

if not cap.isOpened():
    print("Error occured. Couldn't open camera")
    exit()

while True:
    ret, frame = cap.read() #ret is a boolean value that checks whether there is a frame or not

    cv2.imshow("live",frame)

    out.write(frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()