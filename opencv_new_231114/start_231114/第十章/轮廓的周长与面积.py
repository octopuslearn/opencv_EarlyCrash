import cv2
import numpy as np

img = cv2.imread('diansai_small.jpg')
img = cv2.resize(img,None,fx=0.5,fy=0.5)
# print(img.shape)
#转换成单通道
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#二值化 ###ret-是否成功
ret,threshold = cv2.threshold(gray,110,255,cv2.THRESH_BINARY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
threshold_out = cv2.morphologyEx(threshold,cv2.MORPH_OPEN,kernel)


# print(threshold.shape)

#查找轮廓，参2-RETR_EXTERNAL只查找最外部的轮廓，RETR_TREE从大到小从右到左，RETR_CCOMP从里到外，从右到左，每层最多两级。参3-CHAIN_APPROX_SIMPLE只保留角点
# image, contours, hierarchy = cv2.findContours(threshold_out, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# image, contours, hierarchy = cv2.findContours(threshold_out, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
image, contours, hierarchy = cv2.findContours(threshold_out, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, 1, (255,0,0),3)
cv2.drawContours(img, contours, 2, (0,255,0),3)
cv2.drawContours(img, contours, 3, (0,0,255),3)

#计算面积
area = cv2.contourArea(contours[1])
print(area)
area_1 = cv2.contourArea(contours[2])
print(area_1)
area_2 = cv2.contourArea(contours[2])
print(area_2)
# 363708.5
# 501764.0
# 501764.0
# print('area=%d'%(area))

#计算周长
len = cv2.arcLength(contours[1],True)   #闭合2513.521859049797
print(len)
len_1 = cv2.arcLength(contours[1],False)    #不闭合只算了三条边，少算了一个宽2500.521859049797
print(len_1)
# cv2.imshow('contours',contours)
# print(contours)
# cv2.imshow('threshole',threshold)
# cv2.imshow('threshold_out',threshold_out)
# cv2.imshow('gray',gray)
cv2.imshow('img',img)
while True:
    key = cv2.waitKey(1)
    if key & 0xff == ord('q'):
        break

cv2.destroyAllWindows()