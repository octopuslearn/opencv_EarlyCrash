import cv2
import numpy as np

skirt = cv2.imread('../skirt_1.jpg')
print(skirt.shape) #(604, 403, 3)
# 缩放图片参1-图片，参2-缩放后图片大小（a,b）,参3，4-x,y轴缩放比例，缩放算法
# 参2 和 参3,4只使用一个 默认算法双线性插值 cv2.INTER_LINEAR
# out = cv2.resize(skirt, None, fx=0.5,fy=0.5,interpolation=cv2.INTER_LINEAR) #默认，双线性插值，4个像素的加权平均值，图像较好，速度较快
# out_1 = cv2.resize(skirt, None, fx=0.5,fy=0.5,interpolation=cv2.INTER_CUBIC)#双三次插值 16个像素
# out_2 = cv2.resize(skirt, None, fx=0.5,fy=0.5,interpolation=cv2.INTER_NEAREST)#最近邻插值 最快，效果最差
# out_3 = cv2.resize(skirt, None, fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)#适合缩小图像
# out_4 = cv2.resize(skirt, None, fx=0.5,fy=0.5,interpolation=cv2.INTER_LANCZOS4)#Lanczos插值 8*8个像素，放大时质量好，计算开销大

out = cv2.resize(skirt, None, fx=1.5,fy=1.5,interpolation=cv2.INTER_LINEAR) #默认，双线性插值，4个像素的加权平均值，图像较好，速度较快
out_1 = cv2.resize(skirt, None, fx=1.5,fy=1.5,interpolation=cv2.INTER_CUBIC)#双三次插值 16个像素
out_2 = cv2.resize(skirt, None, fx=1.5,fy=1.5,interpolation=cv2.INTER_NEAREST)#最近邻插值 最快，效果最差
out_3 = cv2.resize(skirt, None, fx=1.5,fy=1.5,interpolation=cv2.INTER_AREA)#适合缩小图像
out_4 = cv2.resize(skirt, None, fx=1.5,fy=1.5,interpolation=cv2.INTER_LANCZOS4)#Lanczos插值 8*8个像素，放大时质量好，计算开销大
print(out.shape)

while True:

    cv2.imshow('skirt', skirt)
    cv2.imshow('out', out)
    cv2.imshow('out_2', out_2)
    cv2.imshow('out_3', out_3)
    cv2.imshow('out_4', out_4)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()