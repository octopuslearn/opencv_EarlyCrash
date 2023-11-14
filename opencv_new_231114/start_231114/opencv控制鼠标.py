import cv2
import numpy as np

cv2.namedWindow('mouse', cv2.WINDOW_NORMAL)
cv2.resizeWindow('mouse', 640, 480)

#event-鼠标事件（按下的情况);x,y-鼠标坐标;flags-组合键（鼠标+键盘）;userdata-传递的参数
def mouse_callback(event, x, y, flags, userdata):
    print(event,x,y,flags,userdata)

#鼠标回调函数，参1-窗口名，参2-回调函数，参3-传递的参数
cv2.setMouseCallback('mouse', mouse_callback, '123q')

#显示窗口和背景
##创建了个黑色背景
###参1-行的个数（列），列的个数（行），3个通道；参2-数据类型uint8
mouse = np.zeros((480,640,3),np.uint8)

while True:
    cv2.imshow('mouse', mouse)
    key = cv2.waitKey(1)
    if key & 0xff == ord('q'):
        break


cv2.destroyAllWindows()