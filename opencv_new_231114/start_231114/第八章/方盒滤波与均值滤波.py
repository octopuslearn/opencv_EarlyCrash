# 方盒滤波

import cv2
import numpy as np
skirt = cv2.imread('../skirt_1.jpg')
cv2.imshow('skirt',skirt)


# 均值滤波
##参1-原图，参2-卷积核大小，参3-锚点，参4-边界类型
blur_skirt = cv2.blur(skirt, (3,3))
cv2.imshow('blur_skirt',blur_skirt)

# 方盒滤波3
# 一般也不用方盒滤波 默认是均值滤波（normailze=True 等同于均值滤波）
# 所谓归一化如（5，5）卷积核 需要将所有的数的和/25
# normalize=False 不是均值滤波 也就是不进行归一化 
# normailze=True 等同于均值滤波
###方盒滤波太狠了normalize=False
boxFilter_skirt_false = cv2.boxFilter(skirt,-1,(3,3),normalize=False)
cv2.imshow('boxFilter_skirt_false',boxFilter_skirt_false)

boxFilter_skirt_true = cv2.boxFilter(skirt,-1,(3,3),normalize=True)
cv2.imshow('boxFilter_skirt_true',boxFilter_skirt_true)
while True:

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
