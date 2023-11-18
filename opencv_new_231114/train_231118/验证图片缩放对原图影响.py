"""
#注意：是宽度，高度
cat_1 = cv2.resize(cat_1,(small_w,small_h))
"""
import cv2
import numpy as np
"""
测试了cv2.resize 不会改变原图
img = np.full((480,640,3),(255,0,0), np.uint8)
print(img.shape)
#cv2.resize 不会改变原图
img_size = cv2.resize(img, None, None,0.7,0.7,interpolation=cv2.INTER_LINEAR)
print(img_size.shape)   #访问Mat属性
# print(img_size.size)    #访问图片占用的内存空间
# print(img_size.dtype)   #访问元素的位深，即数据类型
# print(img.shape)
"""

cat_1 = cv2.imread('./cat_1.jpg')
# print(cat_1.shape)
cat_2 = cv2.imread('./cat_2.jpg')
#print(cat_2.shape)


def resize_image(img_1,img_2):
    h, w, ch = img_1.shape
    h_2, w_2, ch_2 = img_2.shape
    small_h, small_w = 0, 0
    if h != h_2 or w != w_2:
        if h <= h_2:
            small_h = h
        else:
            small_h = h_2
        if w <= w_2:
            small_w = w
        else:
            small_w = w_2
        return small_w,small_h
        #错误：问如何在函数中将图片处理好 img_1 = cv2.resize(img_1, (small_w, small_h))
        #错误：问如何在函数中将图片处理好 img_2 = cv2.resize(img_2, (small_w, small_h))


"""
法1

# 注意：是宽度，高度
h,w,ch = cat_1.shape
h_2,w_2,ch_2 = cat_2.shape
small_h,small_w = 0,0
if h != h_2 or w != w_2:
    if h<=h_2:
        small_h = h
    else:
        small_h =h_2
    if w<=w_2:
        small_w = w
    else:
        small_w = w_2
#注意：是宽度，高度
cat_1 = cv2.resize(cat_1,(small_w,small_h))
cat_2 = cv2.resize(cat_2,(small_w,small_h))
# print(cat_1.shape,cat_2.shape)
"""


w,h=resize_image(cat_1,cat_2)
cat_1 = cv2.resize(cat_1,(w,h))
cat_2 = cv2.resize(cat_2,(w,h))

#两图片融合
#注意：图片必须大小相同才能相融
out = cv2.addWeighted(cat_1,0.5,cat_2,0.5,0)



while True:
    cv2.imshow('out',out)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()