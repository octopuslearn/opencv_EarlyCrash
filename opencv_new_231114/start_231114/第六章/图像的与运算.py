import cv2
import numpy as np

show = np.full((480, 640, 3), 0, np.uint8)
show_2 = np.full((480, 640, 3), 0, np.uint8)
cv2.imshow('show', show)
show[50:250,50:250] = (0,255,0)
cv2.imshow('show_now', show)
# 深拷贝，将绿色的方块也拷贝过来了
# show_2 = show.copy()
# show_2[100:300,100:300] = (0,255,0)   #与操作 或操作 异或操作使用
show_2[100:300,100:300] = (255,0,0)     #测试了一下异或 蓝色和绿色异或 交叉的部分青色？？？

cv2.imshow('show_2', show_2)
while True:
    # out = cv2.bitwise_and(show, show_2)
    # cv2.imshow('out', out)
    # out_2 = cv2.bitwise_or(show, show_2)
    # cv2.imshow('out_2', out_2)

    out_3 = cv2.bitwise_xor(show, show_2)
    cv2.imshow('out_3', out_3)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
