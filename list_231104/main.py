"""
列表：
    1.定义列表
    2.列表下标
    3.列表取值
"""

# list1 = [1,2,3,'龙王被群员固定在墙上龙王被群员固定在墙上']
# list2 = [1,['s','win~~~']]  #列表嵌套列表 #要list2[1][0],被嵌套的列表['s','win~~~']在list2的1号元素，'s'在被嵌套的列表的0号元素>>-打印出's'
# print(list1)
# print(list2)
# print(list2[1])
# print(list2[1][0])
# [1, 2, 3, '龙王被群员固定在墙上龙王被群员固定在墙上']
# [1, ['s', 'win~~~']]
# ['s', 'win~~~']
# s


"""
列表的操作方法
    1.insert方法
        insert用于向列表中插入元素
            参1 插入位置
            参2 插入对象
    2.clear函数用于清空列表
    3.remove 移除元素（重复的，只移除第一个）
    4.pop 移除指定位置元素，默认情况下移除最后一个元素，返回要移除的数据
    #注意:参数是下标
    
    5.index 返回元素下标
        参1：查找元素
        参2：起始位置
        参3：结束位置
    6.reverse 将列表逆向排序
    7.extend 将列表补充到另一个列表#[1, 2, 3, 4, 5, 6] 原有列表基础上添加 #不浪费内存空间
    8.append                   #[1, 2, 3, [4, 5, 6]]
    9.加法 不是在原列表上加，而是在一个新的列表上#浪费内存空间
    10.copy 创建副本 两个不会影响
        d = [1,2,3]
        c = d.copy()
        print(c)
    11.赋值操作 两个不会影响
        e = [1,2]
        f = e
        print(f)
        # del e[0]
        # print(e)    #[2]
        # print(f)    #[2]
        
        del f[0]
        print(e)    #[2]
        print(f)    #[2]
    12.sort ASCII排序 不同类型不能排序
        aaa = ['a','吃饭','as','z'] #['a', 'as', 'z', '吃饭']   #ASCII排序
        aaa.sort()
        print(aaa)
    13.count 统计元素在列表中出现的次数
            没有就返回0
"""

# a = ['s','s','a','b'] #移除第一个相同元素
# a.remove('s')
# print(a)
#
# a = ['sss','bss','aaa','sss']   #移除第一个相同元素['bss', 'aaa', 'sss']
# a.remove('sss')
# print(a)
# a = ['s','bs','a','s']
# a.pop(0)
# print(a)
# print(a.pop(0)) #bs
#
#
#
#
#
# a = [1,2,3]
# b=[4,5,6]
# # a.extend(b) #[1, 2, 3, 4, 5, 6]
# # print(a)
# a.append(b) #[1, 2, 3, [4, 5, 6]]
# print(a)
#
#
#
#
# d = [1,2,3]
# c = d.copy()
# print(c)
# e = [1,2]
# f = e
# print(f)
# # del e[0]
# # print(e)    #[2]
# # print(f)    #[2]
# del f[0]
# print(e)    #[2]
# print(f)    #[2]







a = ['a','s','c']   #['a', 'c', 's']    #ASCII排序
a.sort()
print(a)
aa = ['a','as','z'] #['a', 'as', 'z']
aa.sort()
print(aa)

aaa = ['a','吃饭','as','z'] #['a', 'as', 'z', '吃饭']   #ASCII排序
aaa.sort()
print(aaa)

C = [1,2,3,11,34536,0]  #[0, 1, 2, 3, 11, 34536]
C.sort()
print(C)
C = [1,2,3,11,34536,0]  #[0, 1, 2, 3, 11, 34536]升序
C.sort(reverse=True)    #[34536, 11, 3, 2, 1, 0]降序
print(C)

# C = [1,2,3,11,34536,0,'chu']  #不同类型不能排序
# C.sort()
# print(C)