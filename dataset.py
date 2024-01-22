import cv2

img = []

for x in range(1,10):
    img.append(cv2.imread("source/dataset/plant{number}.jpg".format(number = x)))

i = 1;
for y in img:
    y = cv2.resize(y,(216,216))
    grey = cv2.cvtColor(y,cv2.COLOR_BGR2GRAY)
    #cv2.imwrite("source/manipulated/copy{number}.jpg".format(number = i),grey)

    cv2.imshow("plants",grey)
    cv2.waitKey(1000)
    i += 1;

cv2.destroyAllWindows()
