#importing necessary packages
import cv2

#gathering image information
img = cv2.imread("source/cat/cat5.jpg")

if img is None:
    print("Image not found")
else:
    img = cv2.resize(img, (450, 260))

grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#importing cascade document
cat = cv2.CascadeClassifier("source/cat/cat.xml")
cats = cat.detectMultiScale(grey,1.1,2,minSize=(60,60))

cat_crop = []

#reflecting every cat caught in picture
for (i,(x,y,w,h)) in enumerate(cats):
    cv2.rectangle(img,(x,y),(x+w,y+h),(249,188,35),2)
    cv2.putText(img,"cat #{}".format(i+1),(x+4,y-8),cv2.FONT_HERSHEY_SIMPLEX,0.75,
                (249,188,35),2)
    cat_crop.append(img[y:y + h, x:x + w])


for cat in cat_crop:
    cv2.imshow("cat",img)
    cv2.imshow("clipped cat",cat)
    cv2.waitKey(0)

cv2.destroyAllWindows()

