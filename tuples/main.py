#元组中元素值不可更改
#元组可索引，截取，加，乘

tup1 = ()   #空元组
tup3 = 's',1,"weida"
print(tup3) #不需要括号也行
#注意
tup2 = ('s')    #<class 'str'>  当元组只有一个元素时必须加逗号，否则会被当做运算符使用
print(type(tup2))
tup2_1 = ('s',) #<class 'tuple'>
print(type(tup2_1))

#元组中的元素值不可删除，但可以用del删除整个元组--->删除后tup2_1成了未定义
# del tup2_1  #NameError: name 'tup2_1' is not defined.
# print(tup2_1)

tup4 = (1,2,3,4,5,6,'a','s')
print(len(tup4))    #8
print(tup4[1:5])    #(2, 3, 4, 5)
print(tup4[1:5]*2)  #(2, 3, 4, 5, 2, 3, 4, 5)
print(tup4+tup1)    #(1, 2, 3, 4, 5, 6, 'a', 's')



for x in tup4:
    print(x)

