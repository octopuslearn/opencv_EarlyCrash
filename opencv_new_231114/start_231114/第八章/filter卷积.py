import cv2
import numpy as np
skirt = cv2.imread('../skirt_1.jpg')

# 平均卷积核对图像进行了平均模糊
# 平均卷积核：图片的平滑与去噪
# 表示一个权重均值为1/25的平均卷积核
kernel = np.ones((5,5), np.float32)/25
# 参1-原图，参2-位深（-1表示与原图一致），参3-卷积核，参4-锚点（默认(-1，-1)即自己会根据卷积核计算），参5-给卷积后的值加多少，可以不加 参6-边界类型
# 二维卷积函数
out_skirt_1 = cv2.filter2D(skirt,-1,kernel)
cv2.imshow('out_skirt_1', out_skirt_1)


# 平均卷积核越小，则图片的模糊效果越小
kernel_2 = np.ones((2,2), np.float32)/4
out_skirt_2 = cv2.filter2D(skirt,-1,kernel_2)
cv2.imshow('out_skirt_2', out_skirt_2)


while True:
    cv2.imshow('skirt',skirt)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
