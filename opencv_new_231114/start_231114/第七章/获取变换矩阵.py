import cv2
import numpy as np

skirt = cv2.imread('../skirt_1.jpg')
print(skirt.shape)
#错误：返回值有三个不能只有两个变量接收    h,w = skirt.shape #高宽
h,w,ch = skirt.shape
print(h,w,ch)

"""
获取变换矩阵-法1
"""
#注意：此处是逆时针旋转
#参1-中心点，参2-角度，参3-缩放比例
# M = cv2.getRotationMatrix2D((w/2,h/2),30,0.5)    #图片中心为中心点，缩小0.5 逆时针旋转30°
# print(skirt.shape)  #原始图像没有发生变化
#
# out = cv2.warpAffine(skirt,M,(w,h))

"""
获取变换矩阵-法2
getAffineTransform(src,dst)
缩放，平移是根据三角形的对应关系改变的
# 用三个点确定到底是平移旋转缩放，三个点构成了一个三角形，第一个点起点，第二个点横，第三个点竖
"""
# 用三个点确定到底是平移旋转缩放，三个点构成了一个三角形，第一个点起点，第二个点横，第三个点竖
# src = np.float32([[0,0], [400,0] ,[0, 600]])    #旋转
# dst = np.float32([[400,0],[0,0],[400,600]])
src = np.float32([[0,0], [400,0] ,[0, 600]])    #缩放
dst = np.float32([[200,0],[0,0],[200,300]])
M = cv2.getAffineTransform(src,dst)

out = cv2.warpAffine(skirt,M,(w,h))

while True:
    cv2.imshow('skirt',skirt)
    cv2.imshow('out',out)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
