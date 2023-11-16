import cv2
import numpy as np


img = cv2.imread('../cat_1.jpg')
print(img.shape)  # 访问Mat属性(853, 1280, 3)-高度，长度，通道数

print(img.size)  # 占用的内存空间 高度*长度*通道数=853*1280*3

print(img.dtype)    # 元素的位深 uint8
while True:

    cv2.imshow('img', img)
    if (cv2.waitKey(1) & 0xff == ord('q')):
        break

cv2.destroyAllWindows()