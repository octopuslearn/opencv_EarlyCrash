"""
Mat(图片)由hander和data构成
所谓浅拷贝只拷贝了header没有拷贝data,s使得data公用：所以更改cat_1_copy会影响cat_1
默认浅拷贝cat_1_copy = cat_1

深拷贝 拷贝data
cat_2_copy = np.copy(cat_2)
所以更改拷贝后的不会影响拷贝前的
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

cat_1_copy = cat_1
print('cat_1_copy',cat_1_copy.shape)
# 浅拷贝
cat_1_copy[0:100,0:100] = (0,0,255)
cv2.imshow('cat_1_copy_1', cat_1_copy)
cv2.imshow('cat_1', cat_1)

#深拷贝
cat_2_copy = np.copy(cat_2)
cat_2_copy[0:100,0:100] = (0,255,0)
cv2.imshow('cat_2_copy', cat_2_copy)
cv2.imshow('cat_2', cat_2)



while True:
    # cv2.imshow('img',img)
    # cv2.imshow('img_2', img_2)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()