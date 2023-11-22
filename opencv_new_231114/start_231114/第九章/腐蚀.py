import cv2
import numpy as np

#彩色图
skirt = cv2.imread('math.png')


#字母
img = cv2.imread('j.png')
cv2.imshow('img', img)


print(skirt.shape)
skirt = cv2.resize(skirt,None,fx=0.2,fy=0.2)
skirt_gray = cv2.cvtColor(skirt,cv2.COLOR_BGR2GRAY)
print('gray',skirt_gray.shape)
# cv2.imshow('skirt_gray', skirt_gray)

kernel = np.ones((3,3), np.uint8)
#错的kernel是卷积核 skirt_erode = cv2.erode(skirt_gray, 3, 1)
# 灰度图
skirt_erode = cv2.erode(skirt_gray, kernel, 3)
# cv2.imshow('skirt_erode', skirt_erode)
# 彩色图
skirt_erode_1 = cv2.erode(skirt, kernel, 3)
# cv2.imshow('skirt_erode_1', skirt_erode_1)
print('erode',skirt_erode.shape)


#图像腐蚀函数cv2.erode
#必须要有的参数 参1-输入图像，参2-卷积核（需要自己构建np.zeros((3,3),np.uint8)

#参4-锚点默认(-1,-1)
#参5-iteration(迭代器) 默认为1，迭代次数
#参6-borderType边界处理方式
#参7-图像边界处理方式

#错误的：错误理由：erode参数很多，第三个参数不是iterations(迭代器)   img_erode = cv2.erode(img, kernel, 1)
# img_erode = cv2.erode(img, kernel, iterations=1)
# cv2.imshow('img_erode', img_erode)
# img_erode_1 = cv2.erode(img, kernel, iterations=3)
# cv2.imshow('img_erode_1', img_erode_1)

kernel_1 = np.ones((8,8),np.uint8)
img_erode_2 = cv2.erode(img, kernel_1, iterations=1)
cv2.imshow('img_erode_2', img_erode_2)
while True:

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
