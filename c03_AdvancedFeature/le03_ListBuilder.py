# 列表生成式
# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式
# 举个例子，要生成list[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))
print(list(range(1, 11)))

# 但是如果要生成[1x1, 2x2, ..., 10x10]怎么做？方法一是循环
L = []
for x in range(1, 11):
    L.append(x*x)
print(L)

# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list
print([x * x for x in range(1, 11)])
# 写列表生成式时，要把生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
# for循环后面开可以加上if判断，这样我们就可以筛选出仅偶数的平方：
print([x * x for x in range(1, 11) if x % 2 == 0])

# 还可以使用两层循环，可以生成全排列：
print([m + n for m in 'ABC' for n in 'XYZ'])
# 三层和三层以上的循环就很少用到了

# for循环其实可以同时使用两个甚至多个变量， 比如dict的items()可以同时迭代key和value
# 因此，列表生成式也可以使用两个变量来生成list:
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

# 把list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])


# Homework： 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错
L = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L if isinstance(s, str)])



