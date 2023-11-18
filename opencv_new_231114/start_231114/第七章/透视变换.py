import cv2
import numpy as np

skirt = cv2.imread('./123.png')
print(skirt.shape)

src = np.float32([[100,1100],[2100,1100],[0,4000],[2500,3900]])
dst = np.float32([[0,0],[2300,0],[0,3000],[2500,3000]])
# 透视变换的变换矩阵 是四个点 矩形的四个点
M = cv2.getPerspectiveTransform(src,dst)
out = cv2.warpPerspective(skirt,M,(2024,4032))

#错误：返回值有三个不能只有两个变量接收    h,w = skirt.shape #高宽


while True:
    cv2.imshow('out', out)
    cv2.imshow('skirt',skirt)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
