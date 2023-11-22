import cv2
import numpy as np

skirt = cv2.imread('math.png')
print(skirt.shape)
skirt = cv2.resize(skirt,None,fx=0.2,fy=0.2)
skirt_gray = cv2.cvtColor(skirt,cv2.COLOR_BGR2GRAY)
print(skirt_gray.shape)
#错的：使用resize不会更改灰度图的大小skirt_gary = cv2.resize(skirt_gray,None,fx=0.5,fy=0.5)

retval,skrit_threshold = cv2.threshold(skirt_gray,180,255,type=cv2.THRESH_BINARY_INV)
cv2.imshow('skrit_threshold',skrit_threshold)
cv2.imshow('skirt_gray', skirt_gray)

#自适应阈值处理函数 处理光照不均或变化的图像非常有用
###这些参数必须有个
#参2-maxValue-大于阈值时设置的值通常255
#参3-adaptiveMethod-自适应阈值处理方法 cv2.ADAPTIVE_THRESH_MEAN_C 或者cv2.ADAPTIVE_THRESH_GAUSSIAN_C
#参4-thresholdTyepe-阈值类型cv2.THRESH_BINARY 或 cv2.THRESH_BINARY_INV
#参6-blockSize-领域大小它决定了周围多大的区域会被考虑 块的大小为奇数
#参7-C从计算的平均值或加权平均值中减去的常数，用于微调阈值。通常为正数
skirt_adaptive = cv2.adaptiveThreshold(skirt_gray,maxValue=255,adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       thresholdType=cv2.THRESH_BINARY, blockSize=3, C=0)

skirt_adaptive_1 = cv2.adaptiveThreshold(skirt_gray,maxValue=255,adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C,
                                       thresholdType=cv2.THRESH_BINARY, blockSize=11, C=0)

cv2.imshow('skirt_adaptive',skirt_adaptive)
cv2.imshow('skirt_adaptive_1',skirt_adaptive_1)


while True:

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()