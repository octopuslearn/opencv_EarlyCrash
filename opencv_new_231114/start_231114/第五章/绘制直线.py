import cv2
import numpy as np

img = np.ones((500,500,3), np.uint8)    #(500,)
print(img.shape)

while True:
    cv2.imshow('img', img)

    # 直线（x,y）-列，行   默认使用的是LINE_8更加平滑
    cv2.line(img, (0,500), (100,300), (0,0,255),thickness=3, lineType=cv2.LINE_4)    #斜线
    cv2.line(img, (100, 0), (100, 500), (255, 0, 0), thickness=3, lineType=cv2.LINE_4)  # 竖线
    cv2.line(img, (0,100), (500,100), (0,0,150),thickness=1, lineType=cv2.LINE_4)  #横线

    cv2.line(img, (0, 150), (500, 150), (0, 0, 150), thickness=1, lineType=cv2.LINE_8)  # 横线,LINE_8和LINE_4看起来没啥区别

    # 圆形 thickness=负值 填充
    cv2.circle(img, (255, 255), 30, (255,0,0))
    cv2.circle(img, (300,300), 100, (255,255,255),thickness=-1)
    # 矩形 左上角坐标，右上角坐标
    cv2.rectangle(img, (300,0),(500,200),(0,255,0),thickness=3)

    #椭圆 注意：是从最右边开始算起始角度的
    ##圆心，（半长轴，半短轴），旋转角度，起始角度，终止角度
    cv2.ellipse(img,(150,100),(50,25),0,0,270, (0,0,255),thickness=1)
    cv2.ellipse(img, (150, 100), (50, 25), 90, 90, 270, (0, 100, 200), thickness=-1)

    # 多边形 注意：填充方法不同 注意：必须使用int32
    ##顶点坐标（元组，或者列表），[pts]是指将元组包装成列表     方括号[]用于创建列表，而[pts]是一个包含一个元素（变量pts）的列表文字。
    pts = np.array([(0,0),(180,200),(40,400)], np.int32)
    cv2.polylines(img, [pts], True,(255,255,255))


    # 多边形的填充
    cv2.fillPoly(img, [pts], (255,255,255))




    #画文本
    #其实位置，字体，缩放因子，颜色，   bottomLeft0right=True时从起始点从左下角开始，False时从左上角开始
    cv2.putText(img, 'hao_f', (0,100),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=3,color=(0,0,255),thickness=3,lineType=cv2.LINE_4,
                bottomLeftOrigin=False)


    if cv2.waitKey(1) & 0xff == ord('q'):
        cv2.imwrite('./tuxing.jpg', img)
        break

cv2.destroyAllWindows()