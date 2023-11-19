"""
图片的分割与合并
split merge

图片的分割后成了3个单通道的灰度图 感觉只有r通道与其他的通道有很大的不同
图片合并后肉眼没看出和原图有啥区别

图片合并的前提 位深 大小相同
这样的话，两张不同的图片（位深，大小相同）也可以合并
两张图合并的话，会有另一张图某一通道,或者某两种通道的的颜色

"""

import cv2
import numpy as np
img = cv2.imread('./chun.jpg')
img_2 = cv2.imread('./chun_2.jpg')
print(img.shape, img_2.shape)

img = cv2.resize(img, None,fx=0.5,fy=0.5,interpolation=cv2.INTER_LINEAR)
img_2 = cv2.resize(img_2, None,fx=0.5,fy=0.5,interpolation=cv2.INTER_LINEAR)
print(img.shape, img_2.shape)
print(img.dtype, img_2.dtype)

b,g,r = cv2.split(img)  #(900, 1349)两通道的
print(b.shape)
# cv2.imshow('b', b)
# cv2.imshow('g', g)
# cv2.imshow('r', r)

b_2,g_2,r_2 = cv2.split(img_2)
# cv2.imshow('b_2', b_2)
# cv2.imshow('g_2', g_2)
# cv2.imshow('r_2', r_2)

img_out = cv2.merge((b,g,r))
img_2_out = cv2.merge((b_2,g_2,r_2))
# 两张图通道融合
img_out_hun = cv2.merge((b,g,r_2))
cv2.imshow('img_out_hun', img_out_hun)
cv2.imshow('img_out', img_2_out)
cv2.imshow('img_2_out', img_2_out)


cv2.imshow('img', img)
cv2.imshow('img_2', img_2)
while True:
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()