# import cv2
#
# img = cv2.imread("opencv_logo.jpg")
# # cv2.imshow("logo",img)
# # cv2.waitKey() #按任意键退出
##opencv存储一张灰度图，需要三张灰度图，存储在第三个维度上
# cv2.imshow("logo",img)
# cv2.imshow('blue',img[:,:,0])
# cv2.imshow('green',img[:,:,1])
# cv2.imshow('red',img[:,:,2])
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    #灰度图---BGR三个彩色通道的图像做加权平均，实际上也是明暗分布
# cv2.imshow('gray', gray)
#
# cv2.waitKey()


#裁剪
# import cv2
#
# img = cv2.imread("opencv_logo.jpg")
#
# crop = img[10:170,40:200] #opencv索引顺序先横行，在纵列。即10-170行，40-200列
# cv2.imshow('crop',crop)
# cv2.waitKey()



# import cv2
# import numpy as np
# img = np.zeros([300, 300, 3], dtype=np.uint8)   #创建黑色画布，范围300*300*3，数据类型uint8即0-255
#
# cv2.line(img, (100, 200), (250, 250), (255, 0, 0), 3)   #画一条线段，起点（100,200），终点（250,250），颜色（255,0,0），线段粗细3
# cv2.rectangle(img, (30, 100), (60, 150), (0, 255, 0), 3)    #画一个正方体，左上角起点（30，100），对角线坐标（60,150），颜色（0,255,0），粗细3
# cv2.circle(img, (150, 100), 20, (0, 0 ,255), 1) #画一个圆，圆心（150,100），直径20，颜色（0,0,255），粗细1像素
# cv2.putText(img, "hello ai", (100, 50), 0, 1, (255, 255, 255), 2, 1)  #字符串，坐标（100,50），0-字体（默认字体），1-缩放系数，（255,255,255）颜色,粗细2，1-线条类型（即实线）
# cv2.imshow('img',img)
# cv2.waitKey()



# #均值滤波器
# import cv2
# #先前图片噪点很多
# img = cv2.imread('plane.jpg')
#
# #高斯滤波器 噪点减少了，但是失去了一些细节
# gauss = cv2.GaussianBlur(img, (5, 5), 0 )   #内核设为5个像素，sum设为0？？？
# median = cv2.medianBlur(img, (5, 5), 0)
#
# cv2.imshow('img',img)
# cv2.imshow('gauss', gauss)
# cv2.imshow('median', median)
# cv2.waitKey()



# #获取图像特征点
# import cv2
#
# image = cv2.imread("opencv_logo.jpg")
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  #获取灰度图
#
# #转角是最简单的特征，提取转角特征很高效，广泛运用
# corners = cv2.goodFeaturesToTrack(gray, 500, 0.1 , 10)   #返回最多500个特征点，特征点质量优于0.1，特征点间像素大于10
#
# #获取特征点后将每一个特征点标记起来
# for corner in corners:
#     x, y = corner.ravel()
#     cv2.circle(image,(int(x), int(y)), 3, (255, 0, 255), -1)
#
# cv2.imshow('corners', image)
# cv2.waitKey()



#模版匹配
import cv2
import numpy as np

image = cv2.imread("poker.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

template = gray[75:105, 235:265]    #选取图像的一个区域作为匹配的模版 横行75-105，纵行235:265这个位置刚好有个菱形

match = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED) #传入模版，待检测图像，使用标准相关匹配算法
locations = np.where(match >= 0.9)  #找出匹配系数>0.9的点

w, h = template.shape[0:2]   #求出模版的长和宽，方便画图

for p in zip(*locations[::-1]): #循环遍历每一个点
    x1, y1 = p[0], p[1]
    x2, y2 = x1 + w, y1 + h
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
cv2.imshow('gray', gray)
cv2.imshow('image',image)
cv2.waitKey()