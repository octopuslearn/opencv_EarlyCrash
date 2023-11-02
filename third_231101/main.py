cute_cat = ['cat','hell','let\'s','go','a','b']
old_dog = ['this','is','a','old','dog',1,2,3,4,5,6]
# print(cute_cat)         #打印结果['cat', 'hell', "let's", 'go', 'a', 'b']
# print(cute_cat[0:4:2])  #0-5，隔1一个。打印结果['cat', "let's"]
#                         #0-3，步长2（即隔1个）
# print(cute_cat[2:])     #从2开始所有的。打印结果["let's", 'go', 'a', 'b']
# print(cute_cat*2)       #打印三遍。打印结果['cat', 'hell', "let's", 'go', 'a', 'b', 'cat', 'hell', "let's", 'go', 'a', 'b']
# print(cute_cat+old_dog) #连接列表。打印结果['cat', 'hell', "let's", 'go', 'a', 'b', 'this', 'is', 'a', 'old', 'dog', 1, 2, 3, 4, 5, 6]
#
#
# #列表元素可改变
# cute_cat[0] = '999' #['999', 'hell', "let's", 'go', 'a', 'b']
# print(cute_cat)
# cute_cat[2:4] = ['a1','a2','a3']  #['999', 'hell', 'a1', 'a2', 'a3', 'a', 'b']
# print(cute_cat)
# cute_cat[2:4] = []  #['999', 'hell', 'a3', 'a', 'b']
#                     #注意：是2:3
# print(cute_cat)
#
# print(cute_cat[-1]) #0



# #末尾添加新元素
# cute_cat.append('喵~')   #['cat', 'hell', "let's", 'go', 'a', 'b', '喵~']
# print(cute_cat)
# #del语句删除元素
# del cute_cat[0] #['hell', "let's", 'go', 'a', 'b', '喵~']
# print(cute_cat)
# #根据值删除元素
# cute_cat.remove('hell') #["let's", 'go', 'a', 'b', '喵~']
# print(cute_cat)
# #使用pop()方法删除列表末尾元素
# cute_cat.pop()  #["let's", 'go', 'a', 'b']
# print(cute_cat)
#
# print(len(cute_cat))



# for magician in cute_cat:
#     print(magician)
#     # cat
#     # hell
#     # let
#     # 's
#     # go
#     # a
#     # b


# for num_val in range(1,5):  #range(1,5)，1-4，不包括5
#                             #range生成一系列可迭代整数
#     print(num_val)
#
# in_val = list(range(5)) #使用range创建数字列表
# print('in_val:> ' + str(in_val))
# print('in_val数据类型:> ' + str(type(in_val)))


#复制列表
#1.使用切片的方法复制列表
# here = cute_cat[:]
# here.append('slepp!!!')
# print(here)
# cute_cat.append('wake###')
# print(cute_cat)
#2.不使用切片的方法复制列表
here = cute_cat[:]
#此处是将here赋值给there而不是将here的副本存储到there--->将there关联到here,两个实际上是同一个列表
#那么添加元素到there的同时也添加到了here,反之亦然
there = here
print("here:>"+str(here))
print("there:>"+str(there))
there.append('i hate you')
print("n_here:>"+str(here))
print("n_there:>"+str(there))
here.remove('i hate you')
print("n2_here:>"+str(here))
print("n2_there:>"+str(there))