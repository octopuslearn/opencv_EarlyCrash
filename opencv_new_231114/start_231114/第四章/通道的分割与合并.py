import cv2
import numpy as np

img = cv2.imread('../skirt_1.jpg')
# print(img)
b,g,r = cv2.split(img)  # 只获得了二维矩阵
print(b.shape)
print(g.shape)
print(r.shape)
b[200:1000, :] = 255 #片-蓝的
g[190, :] = 255 #横线-绿的
r[:, 190] = 255 #竖线-红的
img_2 = cv2.merge((b, g, r))  #合并
while True:
    cv2.imshow('b', b)
    cv2.imshow('g', g)
    cv2.imshow('r', r)
    cv2.imshow('img', img)
    cv2.imshow('img_2', img_2)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
