#解决了画圆半径和圆心不对的bug
###未解决从右往左画不出圆的bug
import cv2
import numpy as np

"""
# 复习np.array以及np.zeros相关操作
img = np.array([29,29], np.uint8)
img_2 = np.array([[28,24],[1,3],[89,0]],np.uint8)
img_3 = np.array([[[5,2,3],[6,7,8]]],np.uint8)

print(img.shape)
print(img)
print('img_2shape',img_2.shape)
print('img_2',img_2)
print('img_3shape',img_3.shape)
print('img_3',img_3)


img_4 = np.zeros((5,2,3),np.uint8)  #5个两行三列的0
print('img_4shape',img_4.shape)
print('img_4',img_4)

img_5 = np.zeros((5),np.uint8)  #1行5列的0
print('img_5shape',img_5.shape)
print('img_5',img_5)
"""


"""
###注意：必须先新建窗口才能使用
"""
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.resizeWindow('img', 640, 480)
img = np.zeros((480, 640, 3), np.uint8)

#！！！错误 global last_value,look
#注意：先定义再使用
last_value = (0,0)
look = 0


def mouse_callback(event, x, y,flags, userdata):
    # print(event, x, y, flags)


    """
    global （python将知道在引用一个全局变量而不是创建一个新的局部变量）
    """
    global last_value,look


    if event == cv2.EVENT_LBUTTONDOWN:
        last_value = (x,y)
    elif event == cv2.EVENT_LBUTTONUP:
        if look == 0:
            print('line')
            #！！！错误 cv2.line('img', last_value, (x,y),(255,0,0))
            cv2.line(img, last_value, (x, y), (255, 0, 0))
            print('line_end')
        elif look == 1:
            print('circle')
            a = ((x - last_value[0]) //2) + last_value[0]
            b = ((y - last_value[1]) //2) + last_value[1]
            banjing = a - last_value[0]
            print('ab:',a,b)
            print(last_value)
            print('xy:',x,y)
            print('banjing',banjing)
            #！！！错误 cv2.circle('img',(a,b),a,(0,255,0))
            cv2.circle(img, (a, b), banjing, (0, 255, 0))
        elif look == 2:
            print('ractangle')
            cv2.rectangle(img,last_value, (x,y),(0,0,255))
        else:
            print("wrong!!!")

cv2.setMouseCallback('img', mouse_callback, 'sa')




while True:
    cv2.imshow('img', img)
    key = cv2.waitKey(1)
    if key & 0xff == ord('l'):  #line
        look = 0
    elif key & 0xff == ord('c'):    #circle
        look = 1
    elif key & 0xff == ord('t'):    #ractangle
        look = 2
    # elif key & 0xff == ord('p'):
    #     look = 3
    # elif key & 0xff == ord('e'):
    #     look = 4


    if key & 0xff == ord('q'):
        break

cv2.destroyAllWindows()