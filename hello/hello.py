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



#组织列表
########以下，除sorted，全是永久的######


#使用之理由：列表排列顺序通常无法预测
ebood.sort()    #按照a-z排序
print(ebood)
ebood.sort(reverse=True)    #按照z-a排序
print(ebood)



print(sorted(ebood))    #临时改变排序，以a-z    ###如何以z-a排序
#没有这种写法ebood.sorted(reverse = True)
print(ebood)    #验证临时改变顺序，原顺序z-a




#倒着打印列表
#即反转排列顺序
ebood.reverse() #相当于撤销
print(ebood)



#确定列表长度
len(ebood)  ###???为啥没有反




#cars = ['a','b','c','d']   
#print(cars[5]) #错误：超范围

#cars = []
#print(cars[-1])    #错误：不可为空时使用
