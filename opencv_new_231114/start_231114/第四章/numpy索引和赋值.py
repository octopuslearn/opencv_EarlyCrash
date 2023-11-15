# import cv2
# import numpy as np
#
# #行个数，列个数
# img = np.zeros([480,640], np.uint8)
# while True:
#     cv2.imshow('img', img)
#     # img[100,100] = 255  #第100行100列的一个元素
#     count = 0
#     while count < 200:
#         # img[0:count] = 255    #0-199行，所有的列
#         # img[0:count,:] = 255    #同上
#         # img[:,0:count] = 255    #0-199列，所有的行
#         #img[:] = 255    #所有的
#         # img[190,count] = 255 #行的个数不变，列的个数变化--->横线
#         # img[count, 190] = 255   #列的个数变化，行的个数不变--->竖线
#         #img[0:count,0:counqt] = 255
#         # img[0:-100,:-200] = 255
#
#         count = count+1
#     key = cv2.waitKey(1)
#     if key &0xff == ord('q'):
#         break
# cv2.destroyAllWindows()



"""
三层
"""

import cv2
import numpy as np

#行个数，列个数
img = np.zeros([480,640,3], np.uint8)
while True:
    cv2.imshow('img', img)
    #img[100,100,0] = 255  #蓝色   第100行100列第一层（蓝）的一个元素
    count = 0
    while count < 200:
        #img[130,count,0] = 255  #蓝色的一条横线
        #img[count,130,2] = 255 #红色的一条竖线
        # img[:] = (255,0,0)  #蓝色
        #img[:,:,0] = 255    #同上
        img[count,:,1] = 255
        count = count+1
    key = cv2.waitKey(1)
    if key &0xff == ord('q'):
        break
cv2.destroyAllWindows()
