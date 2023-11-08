import cv2
import numpy as np

#读入图像
##参1-路径，参2-如何读取这幅图片
##cv2.IMREAD_COLOR:读取一副彩色图像。图像的透明度会被忽略，这是默认参数
##cv2.IMREAD_GRAYSCALE:以灰度模式读入图片
##cv2.IMREAD_UNCHANGED:读入一幅图像，并且包括图像的alpha通道
# img = cv2.imread('first_20231108143905.jpg')    #注意：图片名不能有中文

#显示图像   窗口会自动调整为图像的大小
##参1-窗口名称，参2-图像
# cv2.imshow('img', img)

#键盘绑定函数
##参-ms，程序等待特定的几ms,在这几ms内，倘若按下任意键，会返回按键的ASCII码。若无按键输入会无限期等待按键按下。
# cv2.waitKey(0)
#删除创建的窗口
##参-要删除的窗口
# cv2.destroyAllWindows()







# img = cv2.imread('first_20231108143905.jpg')    #注意：图片名不能有中文
#
# #先创建一个窗口再加载图片
# ##参1-窗口名，参2-默认cv2.WINDOW_AUTOSIZE-窗口自动大小    cv2.WINDOW_NORMAL-可调整窗口大小
# cv2.namedWindow('img', cv2.WINDOW_NORMAL)
# cv2.namedWindow('img_gray', cv2.WINDOW_NORMAL)
# cv2.imshow('img', img)
#
# img_gray = cv2.imread('first_20231108143905.jpg', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('img_gray', img_gray)
# cv2.waitKey(0)   #按键绑定函数
# ###cv2.destroyWindows('img')   #删除指定窗口 #感觉没有起作用
# cv2.destroyAllWindows() #删除所有窗口
#
# #保存图像
# cv2.imwrite('first_gray.png', img_gray)




# import cv2
# import numpy as np
#
# img = cv2.imread('poayql.jpg')
# cv2.imshow('img', img)
# k = cv2.waitKey(0)
# if k == 0x27:
#     cv2.destroyAllWindows()
# elif k == ord('s'): #ord是python内置函数，用于获取给定字符的Unicode码点（整数表示）
#     cv2.imwrite('poayql_gray.jpg', img)
#     cv2.destroyAllWindows()


# import numpy as np
# import cv2
# #matplotlib是python的一个绘图库，里面有绘图方法
# ##注意：matplotlib是RGB
# from matplotlib import pyplot as plt
#
#
# img = cv2.imread('purple_skirt.jpg')
# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([])
# plt.show()



"""
使用摄像头捕获视频
"""
#
# import cv2
# import numpy as np
#
# #cv2.VideoCapture   参-视频文件/设备索引号
# #创建视频捕获对象
# cap = cv2.VideoCapture()
# cap.open(1) #打开摄像头或者视频文件，返回Ture
# ####报错 cap.get(3, 1280)
# ####报错 cap.get(4, 720)
# ####报错 ret = cap.get(3, 1280)
# ####报错 ret = cap.get(4, 720)
# print("视频大小：", cap.get(3), "*", cap.get(4)) #默认视频大小 视频大小： 640.0 * 480.0
# if cap.isOpened():
#     while True:
#         #Capture frame-by-farm 一帧帧捕获视频
#         ret, frame = cap.read() #cap.read() 返1-帧读取正确True,用来查看视频文件是否已经到达结尾
#
#         #Our operations on the frame come here  #我们对框架的操作就到这里
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#         #Dispaly the resulting frame #显示生成帧
#         cv2.imshow('frame', gray)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         print("无法打开视频捕获对象，正在重试……")
#         cap.open(1)
#
# cap.release()
# cv2.destroyAllWindows()




"""
从文件中播放视频
"""
# import cv2
# import numpy as np
#
# cap = cv2.VideoCapture('WIN_20231107_21_57_09_Pro.mp4')
#
# while (cap.isOpened()):
#     ret, frame = cap.read()
#
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     cv2.imshow('gray', gray)
#
#     if(cv2.waitKey(25) & 0xff == ord('q')):   #此处cv2.waitKey()设置了播放每一帧的持续时间，医保情况下25ms
#         break
#
# cap.release()   #释放视频捕获对象以及相关资源
# cv2.destroyAllWindows()

"""
保存视频
"""
# import cv2
# import numpy as np
#
# cap = cv2.VideoCapture(1)
#
# #创建视频编码器对象，用来指定视频编码器的FourCC码（表示特定的视频编码器）
# fourcc = cv2.VideoWriter_fourcc(*'XVID') #*'XVID'---解包元组
# #用于将图像序列保存为视频文件
# ##输出视频名称，帧速率（帧/秒），帧大小（宽度为640，高度为480）
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))   #不支持mp4
#
# while (cap.isOpened()):
#     ret, frame = cap.read()
#     if ret == True:
#         #对视频或图片进行翻转，可以按照水平，垂直，或者水平垂直方向进行翻转
#         #0-水平方向翻转 1-垂直方向翻转 -1-水平垂直方向翻转
#         frame = cv2.flip(frame, 1)
#         ####错的 frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         #图片帧写入视频文件的操作
#         out.write(frame)
#
#         cv2.imshow('output', frame)
#         if cv2.waitKey(25) & 0xff == ord('q'):
#            break
# cap.release()
# out.release()
# cv2.destroyAllWindows()



"""
画线等
"""

# import cv2
# import numpy as np
#
# img = np.zeros((512, 512, 3), np.uint8) #np.zeros创建空的三维数组（矩阵）
#
#
#
# cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 3)   #画线，起始终止坐标
# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



#人脸检测
# import cv2
# import numpy as np
# #用于对象检测，特别是人脸检测和物体识别
# #加载预训练的分类器模型
# face_detectoe = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')    #人脸特征文件
# img = cv2.imread('face.jpg')
# # 使用分类器检测人脸
# ## 返回检测到的对象位置信息的列表。每个检测到的对象都表示为一个矩形，通常由x,y,width,height表示
# faces = face_detectoe.detectMultiScale(img) #检测出来的人脸是坐标x,y,w,h  有几个人脸就有几个
# print(faces)
# for x, y, w, h in faces:    #遍历列表
#     cv2.rectangle(img, pt1=(x, y), pt2=(x+w, y+h), color=[0, 0, 255], thickness=1)
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




#人脸检测
import cv2
import numpy as np
#加载预训练的分类器模型
face_detectoe = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')    #//detectoe探测器

img = cv2.imread('purple_skirt.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    #数据变少
#用于对象检测
# 图像金字塔的层级： detectMultiScale 方法会在不同尺度的图像上运行级联分类器，以便检测不同大小的对象。scaleFactor 决定了图像金字塔的缩放步长。较小的 scaleFactor 值会导致使用更多的尺度层级，而较大的 scaleFactor 值会减少层级的数量。
#
# 检测窗口的尺寸： scaleFactor 的值越小，意味着每个级别的图像金字塔都比前一个级别的图像小，导致检测窗口变小。这可以用于检测小尺寸对象。
#
# 通常情况下，scaleFactor 的值设置为大于1.0的小数，例如 1.1。这意味着每个级别的图像金字塔都比前一个级别的图像大约10%，并且会在不同尺度上检测对象。如果 scaleFactor 太小，可能会导致遗漏一些较小的对象，而如果太大，可能会导致检测到太多的假阳性。
#
# 调整 scaleFactor 可以根据具体的应用需求来优化对象检测性能。通常，您需要根据您希望检测的对象的大小和数据集的特性来选择合适的值。


#用于过滤检测结果的邻居数。增加这个值可以减少假阳性检测。通常设置为3。
face = face_detectoe.detectMultiScale(gray,
                                      scaleFactor=1.01,
                                      minNeighbors=3,
                                      minSize=(80, 80))
print(face)
for x, y, w, h in face:
    cv2.rectangle(img, (x, y), (x+w, y+h), [255, 0, 255], 3)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
