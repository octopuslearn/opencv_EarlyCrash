# 顶帽操作=原图-开运算--->得到噪点
import cv2
import numpy as np

img = cv2.imread('./tophat.png')
cv2.imshow('img', img)
# 卷积核必须足够大，因为噪点很大
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21,21))
out = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
cv2.imshow('out', out)

while True:

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()