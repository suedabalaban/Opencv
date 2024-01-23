import cv2
import numpy as np

img = []
grey = []

for x in range(1,10):
    img.append(cv2.imread("source/dataset/plant{number}.jpg".format(number = x)))

for y in img:
    grey.append(cv2.cvtColor(y, cv2.COLOR_BGR2GRAY))

    for z in grey:
        ret, thresh = cv2.threshold(z,130,200,cv2.THRESH_BINARY)
        cont, a = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(y,cont,-1,(0,0,255),1)

    cv2.imshow("manipulated plants",y)
    cv2.waitKey(0)


cv2.destroyAllWindows()