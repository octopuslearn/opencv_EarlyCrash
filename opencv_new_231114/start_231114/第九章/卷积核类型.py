import cv2
import numpy as np

#字母
img = cv2.imread('j.png')
cv2.imshow('img', img)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))   #矩形
print(kernel)
# [[1 1 1 1 1]
#  [1 1 1 1 1]
#  [1 1 1 1 1]
#  [1 1 1 1 1]
#  [1 1 1 1 1]]

kernel_1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))   #椭圆的四个角都是0
print(kernel_1)

# [[0 0 1 0 0]
#  [1 1 1 1 1]
#  [1 1 1 1 1]
#  [1 1 1 1 1]
#  [0 0 1 0 0]]


kernel_2 = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))   #十字架横线竖线是1，其他是0
print(kernel_2)
# [[0 0 1 0 0]
#  [0 0 1 0 0]
#  [1 1 1 1 1]
#  [0 0 1 0 0]
#  [0 0 1 0 0]]

# out_2 = cv2.erode(img, kernel_2, iterations=1)    #十字架瘦的最少
# cv2.imshow('out_2', out_2)

out_1 = cv2.erode(img, kernel_1, iterations=1)  #椭圆瘦的其次
cv2.imshow('out_1', out_1)

# out = cv2.erode(img, kernel, iterations=1)    #矩形瘦的最多
# cv2.imshow('out', out)
while True:

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
