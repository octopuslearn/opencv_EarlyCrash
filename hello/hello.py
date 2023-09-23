#此种方法较为常用
ebood = []  #创建空列表
ebood.append("youth")   #append方法在列表末尾添加元素
ebood.append('is')
ebood.append("not")
ebood.append("a time of life.")

print(ebood)   


ebood.insert(0, 'my')   #insert方法在任意位置插入元素
ebood.insert(4,"it is a state of ")
ebood.insert(6,'mind')  #['my', 'youth', 'is', 'not', 'it is a state of ', 'a time of life.', 'mind']
                        #在当前位置插入，其余元素会右移
print(ebood) 

del ebood[5]    #删除第五个元素
print(ebood)

#直接删除元素
#错误：只能将str连接到str，而不是列表   print("befor:" + ebood)
print('befor:')
print(ebood)
ebood.remove("it is a state of ")    #报错理由，将单引号写成了双引号
#ebood.remove('it is a state of ')  ###纠正报错无关单双引号，只不过是少个空格
ebood.remove("mind")
print('now:')
print(ebood)
