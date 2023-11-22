import cv2
import numpy as np

#字母
img = cv2.imread('j.png')
#cv2.imshow('img', img)



#对膨胀影响第一大的是卷积核的大小
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

"""
先腐蚀再膨胀
#腐蚀 不能腐蚀的太狠，否则腐蚀会缺少一部分，膨胀不回来
erode = cv2.erode(img,kernel, iterations=2)
cv2.imshow('erode', erode)
#膨胀
out = cv2.dilate(erode,kernel, iterations=2)
cv2.imshow('out', out)

"""



# #膨胀
# out = cv2.dilate(img,kernel, iterations=2)
# cv2.imshow('out', out)
# #腐蚀
# erode = cv2.erode(out,kernel, iterations=3)
# cv2.imshow('erode', erode)

"""
膨胀
out = cv2.dilate(img, kernel, iterations=1)
out_1 = cv2.dilate(img, kernel, iterations=3)
# cv2.imshow('out', out)
# cv2.imshow('out_1', out_1)

kernel_2 = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
out_2 = cv2.dilate(img, kernel_2, iterations=1)
cv2.imshow('out_2', out_2)
"""





"""
白底黑字
白底黑字 腐蚀变成膨胀，膨胀变成腐蚀
"""
img_1 = cv2.imread('j.png')
# cv2.imshow('img', img)
# img_1 = cv2.bitwise_not(img)
cv2.imshow('img_1', img_1)
print(img_1.shape)


#腐蚀
kernal = np.zeros((3,3),np.uint8)
erode = cv2.erode(img_1,kernel, iterations=3)   #黑色扩大
cv2.imshow('erode', erode)

#膨胀
kernal_1 = np.zeros((3,3),np.uint8)
print(kernal_1)
dilate = cv2.dilate(img_1,kernal_1, iterations=3)
cv2.imshow('dilate', dilate)    #黑色缩小

while True:

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()