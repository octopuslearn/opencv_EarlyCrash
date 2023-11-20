import cv2
import numpy as np
skirt = cv2.imread('./zhouwen.png')
skirt_2 = cv2.imread('./gaussian.png')

# 双边滤波 保留边缘的同时对边沿内区域平滑处理
# 参2-双边滤波器直径 越大越平滑 越小图片细节越多
# 参3-控制颜色像色性的标准差，数值越大表示在颜色更宽松的情况下认为颜色相似
# 参4-~空间
##20,50是常见值
skirt_out_1_2 = cv2.bilateralFilter(skirt, 7, 20, 50)
cv2.imshow('skirt_out_1_2',skirt_out_1_2)

skirt_out_1_3 = cv2.bilateralFilter(skirt, 70, 20, 50)
cv2.imshow('skirt_out_1_3',skirt_out_1_3)

skirt_out_1_4 = cv2.bilateralFilter(skirt, 100, 200, 100)
cv2.imshow('skirt_out_1_4',skirt_out_1_4)

while True:
    cv2.imshow('skirt',skirt)
    #cv2.imshow('skirt_2', skirt_2)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()