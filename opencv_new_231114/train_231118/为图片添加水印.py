"""
添加水印流程：
2.获取Logo掩膜 logo是黑色
3.知道放哪
4.将放Logo区域变成黑色
6.倘若Logo有杂色，就把logo提取出来
7.将logo添加到区域
8.将区域放回原图
"""




# 1.获得一个logo
# 2.logo掩模（放logo的地方黑色，其他的白色）
# 3.搞明白放哪
# 4.将要放的区域变成黑色（logo掩膜和要放区域与运算，即将那个区域要放logo的区域变成黑色）
# 5.logo和要放那个区域add运算
# 6.将添加好Logo的区域放回原图

import cv2
import numpy as np

# #获取Logo
# cat_1 = cv2.imread('./cat_1.jpg')
# logo = cv2.imread('./cat_logo.png')
# # print(cat_1.shape,logo.shape)
# #更改Logo大小
# logo = cv2.resize(logo, None, fx=0.3,fy=0.3,interpolation=cv2.INTER_LINEAR)
# # print(logo.shape)
#
# # 将logo区域设置为透明区（黑色）
# logo_1 = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)
# # cv2.imshow('logo_1',logo_1)
# # print(logo_1.shape)
#
# # 提取原始图像中与Logo相关的区域
# ##将放logo区域设置为透明区（黑色）
# cat_1_ym = cat_1[0:188,0:313]
# cat_logo = cv2.bitwise_and(cat_1_ym, cat_1_ym, mask=logo_1)
# # cv2.imshow('cat_logo', cat_logo)
#
#
# #将结果放回原始图像
# cat_1[0:188,0:313] = cat_logo
# cv2.imshow('ok',cat_1)






# # 1.获取logo
# logo = cv2.imread('./cat_logo_red.jpg')
# img = cv2.imread('./cat_2.jpg')
# # print(logo.shape,img.shape) #(2052, 2125, 3) (854, 1280, 3)
# # 中心 高 宽
# # 854//2=427 1280//2=640
# # 410//2=205 425//2=212
# # 高((854//2)-(410//2)) : ((854//2)+(410//2))
# # 宽((1280//2)-(425//2)) : ((1280//2)+(425//2))
# # 222:632
# # 428:852
# logo_small = cv2.resize(logo,None,fx=0.2,fy=0.2)
# # print(logo_small.shape) #(410, 425)
#
#
#
#
#
# # 2.获得Logo掩模
# logo_gray = cv2.cvtColor(logo_small, cv2.COLOR_BGR2GRAY)
# ret,logo_ym = cv2.threshold(logo_gray,200,255,cv2.THRESH_BINARY)
# cv2.imshow('logo_ym',logo_ym)
#
#
#
#
# # 3.搞明白放哪
# fang = img[222:632, 428:853]
# ##报错的理由是：fang和logo_ym图片大小不同
# # print(fang.shape)
# # print(logo_ym.shape)
# # (410, 424, 3)
# # (410, 425)
#
#
#
#
# # 4.将要放logo的区域变成黑色
# ##报错的理由是：fang和logo_ym图片大小不同
# logo_fang = cv2.bitwise_and(fang, fang, mask=logo_ym)
#
#
#
#
# # 5.将logo区域设为透明 要把logo提取出来
# logo_ym_fan = cv2.bitwise_not(logo_ym)
# logo_out = cv2.bitwise_and(logo_small,logo_small,mask=logo_ym_fan)
# w,h,ch = logo_out.shape
# white_img = np.full((w,h,ch),1,np.uint8)*80
# white_img = cv2.bitwise_and(white_img,white_img,mask=logo_ym_fan)
# logo_out = cv2.add(logo_out,white_img)
#
#
#
#
# # 6.将logo添加到要添加的区域
# logo_fang_ok = cv2.add(logo_fang, logo_out)
#
#
#
#
# # 7.将区域放回原图
# img[222:632, 428:853] = logo_fang_ok
# cv2.imshow('img', img)





"""
添加水印流程：
2.获取Logo掩膜 logo是黑色
3.知道放哪
4.将放Logo区域变成黑色
6.倘若Logo有杂色，就把logo提取出来
7.将logo添加到区域
8.将区域放回原图
"""
# 1.获取logo
logo = cv2.imread('./cat_logo_red.jpg')
img = cv2.imread('./cat_2.jpg')
# print(logo.shape,img.shape) #(2052, 2125, 3) (854, 1280, 3)
# 中心 高 宽
# 854//2=427 1280//2=640
# 410//2=205 425//2=212
# 高((854//2)-(410//2)) : ((854//2)+(410//2))
# 宽((1280//2)-(425//2)) : ((1280//2)+(425//2))
# 222:632
# 428:852
logo_small = cv2.resize(logo,None,fx=0.2,fy=0.2)
# print(logo_small.shape) #(410, 425)
# cv2.imshow('logo_samll',logo_small)

# 2.获得Logo掩模 logo是黑的其他白色
logo_gray = cv2.cvtColor(logo_small, cv2.COLOR_BGR2GRAY)
ret,logo_ym = cv2.threshold(logo_gray,200,255,cv2.THRESH_BINARY)
# cv2.imshow('logo_ym',logo_ym)

# 3.搞明白放哪
fang = img[222:632, 428:853]
##报错的理由是：fang和logo_ym图片大小不同
# print(fang.shape)
# print(logo_ym.shape)
# (410, 424, 3)
# (410, 425)

# 4.将要放logo的区域变成黑色
##报错的理由是：fang和logo_ym图片大小不同
logo_fang = cv2.bitwise_and(fang, fang, mask=logo_ym)
# cv2.imshow('logo_fang',logo_fang)

# 5.要把logo提取出来
logo_ym_fan = cv2.bitwise_not(logo_ym)
# cv2.imshow('logo_ym_fan',logo_ym_fan)
logo_out = cv2.bitwise_and(logo_small,logo_small,mask=logo_ym_fan)
cv2.imshow('logo_out',logo_out)
w,h,ch = logo_out.shape
white_img = np.full((w,h,ch),1,np.uint8)*100
white_img = cv2.bitwise_and(white_img,white_img,mask=logo_ym_fan)
logo_out = cv2.subtract(logo_out,white_img)

# 6.将logo添加到要添加的区域
logo_fang_ok = cv2.add(logo_fang, logo_out)

# 7.将区域放回原图
img[222:632, 428:853] = logo_fang_ok
cv2.imshow('img', img)






while True:
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()