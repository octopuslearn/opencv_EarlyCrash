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

ebood_news = ebood.pop()    #弹出最后一个元素(删除元素并使用它,例如需要外星人被杀死的坐标以显示爆炸效果)
print(ebood)
print(ebood_news)   #坐标值
#此方法可获取最新值
print("The latest input value is" + ':' + ebood_news)
