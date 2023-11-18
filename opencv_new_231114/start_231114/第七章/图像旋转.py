import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while cap.isOpened():
    tmp, frame = cap.read()
    if tmp:
        cv2.imshow('show', frame)
        out = cv2.flip(frame, 1)  #左右翻转
        out_1 = cv2.rotate(out, cv2.ROTATE_90_CLOCKWISE)    #顺时针90
        out_2 = cv2.rotate(out, cv2.ROTATE_90_COUNTERCLOCKWISE) #逆时针90
        out_3 = cv2.rotate(out, cv2.ROTATE_180)  #旋转180
        cv2.imshow('flip', out)
        cv2.imshow('out_1', out_1)
        cv2.imshow('out_2', out_2)
        cv2.imshow('out_3', out_3)
        if cv2.waitKey(1000//25) & 0xff == ord('q'):
            break
    else:
        print('摄像头打开失败')
        break

cap.release()
cv2.destroyAllWindows()