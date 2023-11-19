"""
图片的翻转
flip() 1-左右翻转 0-左右翻转 -1-上下左右翻转

图像的旋转
rotate()
"""

import cv2
import numpy as np

cat_1 = cv2.imread('./chun.jpg')
print(cat_1.shape)
cat_2 = cv2.imread('./chun_2.jpg')
print(cat_2.shape)

img = cv2.resize(cat_1, None,fx=0.2,fy=0.2,interpolation=cv2.INTER_LINEAR)
img_2 = cv2.resize(cat_2, None,fx=0.2,fy=0.2,interpolation=cv2.INTER_LINEAR)
print(img.shape, img_2.shape)

"""
flip翻转
img = cv2.flip(img,0)   #0-上下翻转
img_2 = cv2.flip(img_2, 1)  #1-左右翻转
img_xiaokong = np.copy(img)
img_xiaokong = cv2.flip(img_xiaokong, -1)
cv2.imshow('img_xiaokong', img_xiaokong)
"""

"""
图像的旋转 rotate
"""
cv2.imshow('img', img)
cv2.imshow('img_2', img_2)


img_1_1 = cv2.rotate(img,rotateCode=cv2.ROTATE_90_CLOCKWISE)    #顺时针90
cv2.imshow('img_1_1', img_1_1)
img_1_2 = cv2.rotate(img,rotateCode=cv2.ROTATE_180)
cv2.imshow('img_1_2', img_1_2)
img_1_3 = cv2.rotate(img,rotateCode=cv2.ROTATE_90_COUNTERCLOCKWISE) #逆时针旋转90 即顺时针旋转270
cv2.imshow('img_1_3', img_1_3)


while True:


    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()