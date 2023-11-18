import cv2
import numpy as np

skirt = cv2.imread('../skirt_1.jpg')
print(skirt.shape)
#错误：返回值有三个不能只有两个变量接收    h,w = skirt.shape #高宽
h,w,ch = skirt.shape
print(h,w,ch)
# 变换矩阵是个2X2的单位矩阵，平移的话加上偏移量
# 宽高
img = np.float32([[1,0,100],[0,1,200]])   #此为向右平移-列
img = np.float32([[1,0,-100],[0,1,-200]])   #负数则向上向左平移


#错误：参3-输出图片大小（宽，高） out = cv2.warpAffine(skirt,img,(604,403))
out = cv2.warpAffine(skirt,img,(403,604))   #
while True:
    cv2.imshow('out', out)
    cv2.imshow('skirt',skirt)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
