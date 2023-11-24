import cv2
import numpy as np
img = cv2.imread('j.png')
cv2.imshow('img', img)

# 形态学梯度=原图-腐蚀
# 核越小腐蚀的越少，得到的边缘越越细，得到边缘
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,1))
out = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
cv2.imshow('out', out)

while True:

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
