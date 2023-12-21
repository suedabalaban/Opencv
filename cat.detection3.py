import cv2

cap = cv2.VideoCapture(0)
cat = cv2.CascadeClassifier("source/cat/cat.xml")


while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cats = cat.detectMultiScale(grey, 1.1, 2, minSize = (30,30))

    cat_crop = []

    for (i, (x, y, w, h)) in enumerate(cats):
        cv2.rectangle(frame, (x, y), (x + w, y + h), (249, 188, 35), 2)
        cv2.putText(frame, "cat #{}".format(i + 1), (x + 4, y - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                    (249, 188, 35), 2)
        cat_crop.append(frame[y:y + h, x:x + w])

    if ret == 0:
        break
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    cv2.imshow("cats",frame)

cap.release()
cv2.destroyAllWindows()