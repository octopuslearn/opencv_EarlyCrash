# """
# python无需编译
# 大小写敏感
# 缩进代表代码块，无需{}
# 函数与函数间用空行隔开
# """
# #这是单行注释
# '''
# 这是多行注释
# '''
# """
# 这是多行注释
# """
#
# #这是print标准输入，转义字符
# #print打印字符串
# print('si 1 si')
# print("伟大的章鱼哲学")
# print("好家伙\n吃了么您！\t那叫一个地道")
# print(r"好家伙\n吃了么您！\t那叫一个地道")    #在字符串前加r或R取消
# print("这是引号：\"；这是反斜杠\\")
# print("""                               #打印多行文本
# 床前明月光，
# 疑是地上霜。
# 举头望明月，
# 低头思故乡。
# """)
#
#
# """
# 变量类型
# #无需类型声明
# #变量使用前必须赋值，赋值后才会被创建
# 整数 int 长整型（只一种）
# 布尔 bool
# 浮点数 float
# 复数 complex
# """
# in_val = 1
# out_val = 3.33
# name = "kkis,wsxfbs"
# #多变量赋值
# a=b=c=1
# c,d,e=1,'asfa',234.41
# print(type(c),type(d),type(e))
#
#
# print("打印多个值，用逗号隔开", in_val, out_val)
# print("这是in_val:>" + str(in_val) + "\t" + \
#       "这是out_val:>" + str(out_val) + "\t" + \
#       "这是name:>" + str(name))                            #字符串和数字不能一起打印，必须将数字转换成字符串 反斜杠实现多行语句
# print("in_val数据类型:>\t"+str(type(in_val)))
# print("out_val数据类型:>\t"+str(type(out_val)))
# print("name数据类型:>\t"+str(type(name)))
#
# print(name) #kkis,wsxfbs
# print(name[0:3])    #kki打印0-3元素
# print(name[0:-3])    #kkis,wsx打印0-倒数第三个元素
# print(name[0:5:2])  #ki,打印每隔1个字符-变量[头下标:尾下标:步长]
#
#
#
#
# #输入函数
# # num = input("输入：>"); print(num) #同一行可以使用多条语句，用;隔开
# # print(num)
#
#
# #数值运算
# add_i = 10
# add_o = 33.333
# sum = add_o + add_i
# cheng = sum**2 #乘方，即^2
# chu_1 = 4/2   #除法，结果浮点数
# chu_2 = 4//2  #除法，结果整数
# chu_3 = sum/3   #浮点数除法，结果浮点数
# chu_4 = sum//4  #结果被截断为整数10.0
# chu_5 = 5%3
# chu_6 = 5.0%3
# print("sum:>",str(sum))
# print("cheng:>",str(cheng))
# print("chu_1:>",str(chu_1))
# print("chu_2:>",str(chu_2))
#
# print("chu_3:>",str(chu_3))
# print("chu_4:>",str(chu_4))
# # chu_3:> 14.444333333333333
# # chu_4:> 10.0
#
# print("chu_5:>",str(chu_5))
# print("chu_6:>",str(chu_6))
# # chu_5:> 2
# # chu_6:> 2.0


# a = 10;
# b = 20.323;
# c = a**2 + b//2 -(b+1)
# d = c + b%10
# e = b%10
# print(c)
# print(d)
# print(e)
# # 88.67699999999999
# # 89.0
# # 0.3230000000000004



"""
python中没有switch case
但有match case
"""
#if语句
# ex = int(input("请输入：>"))
# print(ex)
# if 20>ex>10:
#     print(">10")
# elif 30>ex>20:
#     print(">20")
# else:
#     print("<=10")

#match case语句
# match ex:
#     case 10:
#         print("10")
#     case 20:
#         print("20")
#     case 30:
#         print("30")
#     case _:
#         print("無")

"""
循环语句
1.for循环
2.while循环
"""

#1.1-while循环
# b_in = int(input("请输入：> "))
# while b_in:
#     print("sss\n")
#     b_in = int(input("请输入：> "))
# print("已退出")


#1.2-while循环1---while else
# b_in = int(input("请输入：> "))
# while b_in:
#     print("sss\n")
#     b_in = int(input("请输入：> "))
# else:
#     print("已退出")

#for 变量 in 可迭代对象
#1.首先获取可迭代对象
#2.每次迭代中for循环从可迭代对象中获取下一个元素，并将其赋值给一个变量
#3.执行for循环中的代码块
# num = [1,2,3,4,5,6,7,8,9,10]
# for s in num:
#     print(s)

num = [1,2,3,4,5,6,7,8,9,10]
for s in num:
    print(s)
else:
    print("结束了")
