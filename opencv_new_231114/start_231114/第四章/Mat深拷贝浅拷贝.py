# Mat包括了两个部分，一个头Header(包含了很多属性)，一个data
import cv2
import numpy as np

# img = np.zeros((200,400), np.uint8)
# # 默认是浅拷贝
# img_2 = img
# img_2[:] = 255
# print(img.shape)
# cv2.imshow('img', img)
# cv2.imshow('img_2', img_2)
# cv2.waitKey()

this_img = np.zeros((500, 800), np.uint8)
cv2.imshow('this_img', this_img)

# 深拷贝
that_img = this_img.copy()
that_img[:] = 255
cv2.imshow('that_img', that_img)
cv2.waitKey()