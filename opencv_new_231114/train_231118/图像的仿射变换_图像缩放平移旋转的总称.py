"""
仿射变换
参5-flags插值算法的标志cv2.INTER_LINEAR 和图片的缩放resize一样的但是多了几个
参6-borderMode边界模式的标志cv2.BORDED_CONSTANT
参7-borderValue边界填充值
warpAffine(img,M,(w,h))


变换矩阵
计算机视觉中用浮点数来表示像素值或者变换矩阵
M-变换矩阵
# 变换矩阵是2*2的单位矩阵
# 平移向量是2*1的，所以平移矩阵是2*3的
# 前两个是单位矩阵，最后一个是偏移量 100-是宽的偏移量，0-是高的偏移量
###！！！注意： 第一列，第二列是缩放系数，第一个是x轴的缩放系数，第二个是y轴的缩放系数
np.float32 = ([[1,0,100],[0,1,0])
"""

import cv2
import numpy as np


cat_1 = cv2.imread('./chun_long.jpg')
print(cat_1.shape)
cat_2 = cv2.imread('./banai.jpg')
print(cat_2.shape)
cat_1 = cv2.resize(cat_1, None,fx=0.5,fy=0.5,interpolation=cv2.INTER_LINEAR)
cat_2 = cv2.resize(cat_2, None,fx=0.7,fy=0.7,interpolation=cv2.INTER_LINEAR)
print(cat_1.shape)

h,w,ch = cat_2.shape
h_2,w_2,ch_2 = cat_1.shape
M_1 = np.float32([[1,0,100],[0,1,0]])
M = np.float32([[0.5,0,100],[0,0.5,0]])

cat_2 = cv2.warpAffine(cat_2,M_1,(w,h))
cv2.imshow('cat_2',cat_2)
#(w_2//2,h_2//2)决定了输出图像的大小，默认是目标图片和原图左上角对齐，所以只剩左上一部分
cat_1_2 = cv2.warpAffine(cat_1,M_1,(w_2//2,h_2//2))
cv2.imshow('cat_1_2',cat_1_2)
cat_1_1 = cv2.warpAffine(cat_1,M,(w_2,h_2))
print(cat_1_1.shape)
cv2.imshow('cat_1_1',cat_1_1)
while True:

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()