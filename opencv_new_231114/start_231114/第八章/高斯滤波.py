import cv2
import numpy as np
skirt = cv2.imread('./gaussian.png')

# 高斯滤波 去除高斯噪点
# 参1-原图，参2-核，参4-sigmaX=x方向上的高斯核标准差，参5-y方向上的高斯标准差，参6-边界类型
gaosi_Blur = cv2.GaussianBlur(skirt,(5,5),sigmaX=1,sigmaY=1)
cv2.imshow('gaosi_Blur', gaosi_Blur)


# 感觉没多少区别
gaosi_Blur_1 = cv2.GaussianBlur(skirt,(5,5),sigmaX=1,sigmaY=5)
cv2.imshow('gaosi_Blur_1', gaosi_Blur_1)
while True:
    cv2.imshow('skirt',skirt)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
