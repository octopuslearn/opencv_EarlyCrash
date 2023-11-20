"""
仿射变换
参4-(w,h)决定了输出图像的大小，默认是目标图和原图左上角对齐
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

"""
自己写变换矩阵
M_1 = np.float32([[1,0,100],[0,1,0]])
M = np.float32([[0.5,0,100],[0,0.5,0]])

cat_2 = cv2.warpAffine(cat_2,M_1,(w,h))
cv2.imshow('cat_2',cat_2)
#(w_2//2,h_2//2)决定了输出图像的大小，默认是目标图片和原图左上角对齐，所以只剩左上一部分 另外黑色部分是窗口太大的缘故
cat_1_2 = cv2.warpAffine(cat_1,M_1,(w_2//2,h_2//2))
cv2.imshow('cat_1_2',cat_1_2)
cat_1_1 = cv2.warpAffine(cat_1,M,(w_2,h_2))
print(cat_1_1.shape)
cv2.imshow('cat_1_1',cat_1_1)
"""


"""
使用API获取变换矩阵
"""
"""
# 法1.获取旋转矩阵
## 参1-旋转中心，参2-旋转角度（逆时针为正），参3-缩放因子
M = cv2.getRotationMatrix2D((w//2,h//2), 30, 1) #以图片中心为圆心，逆时针旋转30°，不缩放
cat_1_out = cv2.warpAffine(cat_1, M, (w,h))

cv2.imshow('cat_1_out', cat_1_out)
cv2.imshow('cat_1',cat_1)
"""

"""
#法2.获取变换矩阵
###感觉此种方法太过麻烦，需要自己计算三个点
src原图的三个点构成的三角形 dst目标图的三个点构成的三角形
都是包含三个点的数组
缩放，平移是根据三角形的对应关系改变的
# 用三个点确定到底是平移旋转缩放，三个点构成了一个三角形，第一个点起点，第二个点横，第三个点竖
###左移- 下移+
"""
src = np.float32([[0,0],[512,0],[512,768]])

dst = np.float32([[512,0],[0,0],[0,768]])   #左右镜像
M = cv2.getAffineTransform(src,dst)
cat_1_out = cv2.warpAffine(cat_1, M, (w,h))
cv2.imshow('cat_1_out',cat_1_out)

dst_2 = np.float32([[0,768],[512,768],[512,0]]) #上下镜像
M_2 = cv2.getAffineTransform(src,dst_2)
cat_1_out_2 = cv2.warpAffine(cat_1, M_2, (w,h))
cv2.imshow('cat_1_out_2',cat_1_out_2)

dst_3 = np.float32([[-100,50],[412,50],[412,818]]) #左移-100，下移50
M_3 = cv2.getAffineTransform(src,dst_3)
cat_1_out_3 = cv2.warpAffine(cat_1, M_3, (w,h))
cv2.imshow('cat_1_out_3',cat_1_out_3)

# src = np.float32([[0,0],[512,0],[512,768]])
dst_4 = np.float32([[100,-50],[612,-50],[612,718]]) #右移100，上移-50
M_4 = cv2.getAffineTransform(src,dst_4)
cat_1_out_4 = cv2.warpAffine(cat_1, M_4, (w,h))
cv2.imshow('cat_1_out_4',cat_1_out_4)


# src = np.float32([[0,0],[512,0],[512,768]])
dst_5 = np.float32([[100,100],[300,100],[300,500]]) #缩小
M_5 = cv2.getAffineTransform(src,dst_5)
cat_1_out_5 = cv2.warpAffine(cat_1, M_5, (w,h))
cv2.imshow('cat_1_out_5',cat_1_out_5)


cv2.imshow('cat_1',cat_1)
while True:

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()














