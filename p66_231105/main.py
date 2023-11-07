"""
isinstance()判断对象是否是某种类型，返回值布尔型
"""

# a = 1
# b = 's'
# c = [1,23]
# d = (1,23,5)
# e =  set([1,3,5])
# f = {'s':1,3:5}
# print(isinstance(a,int))    #True
# print(isinstance(a,float))    #False
#
# print(isinstance(b,str))
# print(isinstance(c,list))
# print(isinstance(d,tuple))
# print(isinstance(e,set))
# print(isinstance(f,dict))
#True
# False
# True
# True
# True
# True
# True


"""
条件语句
    if...elif...else分支语句
"""


# if 1<3:
#     print("ture")
# else:
#     print("flase")
#
#
#
# a = int(input('请输入你的成绩：'))
# if a<3:
#     print('a<3')
# elif a<10:
#     print("a<10")
# else:
#     print("a>=10")


"""
for
    for循环用来历遍序列
    通过不使用下标的方式对每个元素进行访问
    字符串、列表、元组、集合，字典
    注意：字典只历遍键
    
    range(0,10)历遍数字,10取不到
    
    
    ###遍历字典方法:
        a = {
        '2':1,
        1:123,
        's':'weida'
        }
        for i in d.items():
            pirnt(i)
"""
# for i in range(0,10):
#     print(i)
#
# a = {
#     '2':1,
#     1:123,
#     's':'weida'
# }
# print(a.items())    #dict_items([('2', 1), (1, 123), ('s', 'weida')])
# for i in a.items():
#     print(i)
# ('2', 1)
# (1, 123)
# ('s', 'weida')


"""
range()函数步长
    range(0,6,3)
###注意：有步长时必须用for
    print(range(0,6,3)) #range(0, 6, 3)
    for i in range(0,6,2):
        print(i)
"""
# print(range(0,6,3)) #range(0, 6, 3)
# for i in range(0,6,2):
#     print(i)
# 0
# 2
# 4



"""
利用for循环获取
"""
# a = [1,[1,23],[7,8,9]]
# for i in a:
#     print(i)
#1
# [1, 23]
# [7, 8, 9]
# a = [1,[1,23],[7,8,9]]
# for i in a:
#     if isinstance(i,list):
#         print("不是列表：")
#         for ii in i:
#             print(ii)
#     else:
#         print('是列表')
#         print(i)
# 1
# 1
# 23
# 7
# 8
# 9


"""
while 循环
"""
# i = 0
# while i<3:
#     print(i)
#     i += 1
#     if i == 1:
#         continue
#     if i == 2:
#         break
# print('结束')

# 0
# 1
# 2

"""
pass 空语句，为了保持程序结构的完整性
用于语法上必须有什么语句，但程序什么也不做的场合
"""

# for i in range(0,10):
#     pass


"""
函数
    def 创建函数的关键字
    函数参数
"""

def addin():    #创建函数
    print("sss")

addin()         #调用函数