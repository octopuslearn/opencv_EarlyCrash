import cv2
import numpy as np

# skirt = cv2.imread('../skirt_1.jpg')
# print(skirt.shape) #(604, 403, 3)
# # flip(img,a) a=0上下翻转 a=1左右翻转 a<0上下左右翻转
# out = cv2.flip(skirt, 0)
# out_2 = cv2.flip(skirt, 1)
# out_3 = cv2.flip(skirt, -1)
#
# while True:
#
#     cv2.imshow('skirt', skirt)
#     cv2.imshow('out', out)
#     cv2.imshow('out_2', out_2)
#     cv2.imshow('out_3', out_3)
#     # cv2.imshow('out_4', out_4)
#
#     if cv2.waitKey(1) & 0xff == ord('q'):
#         break
# cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)

# # 虽然也对，但不这么写
# while True:
#     if cap.isOpened():
#         tmp,frame = cap.read()
#         if tmp:
#             cv2.imshow('show',frame)
#             if cv2.waitKey(1000 // 25) & 0xff == ord('q'):
#                 break
#     else:
#         print('摄像头打开失败')
#         break
#
#     #错的不能写在这 if cv2.waitKey(1000/25) & 0xff == ord('q'):
#     #错的不能写在这     break


while cap.isOpened():
    if cap.isOpened():
        tmp,frame = cap.read()
        if tmp:
            cv2.imshow('show',frame)
            out = cv2.flip(frame, 1)    #左右翻转
            cv2.imshow('out',out)

            out_2 = cv2.flip(frame, -1) #上下左右都翻转
            cv2.imshow('out_2',out_2)
            if cv2.waitKey(1000 // 25) & 0xff == ord('q'):
                break
    else:
        print('摄像头打开失败')
        break
cap.release()
cv2.destroyAllWindows()