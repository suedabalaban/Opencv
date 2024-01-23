import cv2
import numpy as np

img = []
grey = []

#read every image in source file and append them on an empty list
for x in range(1,10):
    img.append(cv2.imread("source/dataset/plant{number}.jpg".format(number = x)))

#change image colors to grey in order to perform operations more accurately
for y in img:
    y = cv2.resize(y,(512,512))
    grey.append(cv2.cvtColor(y, cv2.COLOR_BGR2GRAY))

    # normalize pixel values and store it in an np array
    normalized = np.empty_like(y,dtype= np.float32)
    cv2.normalize(y, normalized, 0, 1, cv2.NORM_MINMAX)

    #perform findContours method on grey images
    for z in grey:
        ret, thresh = cv2.threshold(z,130,200,cv2.THRESH_BINARY)
        cont, a = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    #show every image with their contoured version on original state
    cv2.drawContours(y,cont,-1,(0,0,255),1)

    cv2.imshow("manipulated plants",y)
    cv2.waitKey(0)


cv2.destroyAllWindows()