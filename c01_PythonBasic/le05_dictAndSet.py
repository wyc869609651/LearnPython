# dict
# Python内置了字典： dict的支持，dict全称dictionary，在其他语言中也称为map,
# 使用（key-value）存储，具有极快的存储速度

scoreDict = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(scoreDict['Michael'])
scoreDict['Adam'] = 67
print(scoreDict['Adam'])
print(scoreDict)
# 由于一个key只能对应一个value,所以，多次对一个key放入value，后面的值会把前面的值覆盖掉
scoreDict['Jack'] = 90
print(scoreDict['Jack'])
scoreDict['Jack'] = 80
print(scoreDict['Jack'])
# 如果key不存在，dict就会报错
# print(scoreDict['Thomas'])
# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在
print('Thomas' in scoreDict)
# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或自己指定的值
print(scoreDict.get('Thomas'))
print(scoreDict.get('Thomas', -1))
# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
scoreDict.pop('Bob')
print(scoreDict)

# set
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，set中没有重复的key
s = set([1, 2, 3])
print(s)
s = set([1, 1, 2, 2, 3, 3])
print(s)
# 通过add(key)方法可以添加元素到set中，可以重复，但不会有效果
s.add(4)
print(s)
s.add(4)
print(s)
# 通过remove(key)方法可以删除元素
s.remove(4)
print(s)
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)
