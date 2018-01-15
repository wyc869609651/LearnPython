# Python内建了map()和reduce()函数
# 一、map
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，
# 并把结果作为新得Iterator返回。
# 举例说明，比如我们有一个函数f(x)=x²，要把这个函数作用在一个list[1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现：
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
# map()传入的第一个参数时f,即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，
# 因此通过list()函数让他把整个序列都计算出来并返回一个list

# 二、reduce：归纳为、减少、缩小
# reduce()把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和
# 序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 把序列[1, 3, 5, 7, 9]变成整数13579,reduce就可以排上用场：

from functools import reduce
def fn(x, y):
    return x * 10 + y

print(reduce(fn, [1, 3, 5, 7, 9]))
# 这个例子本身没多大用处，但是，如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map(),
# 我们就可以写出把str转换为int的函数：
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print(reduce(fn, map(char2num, '13579')))

# 整理成一个str2int的函数就是：
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(string):
    return reduce(lambda x, y: x * 10 + y, map(lambda s: DIGITS[s], string))

print(str2int('12345'))


# 练习1
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范输入。
# 例如：输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    return name[0].upper() + name[1:].lower()

print(list(map(normalize, ['adam', 'LISA', 'barT'])))


# 练习2
# Python提供的sum()函数可以接收一个list并求和， 请编写一个product()函数，可以接收一list并利用reduce()求积

def product(L):
    return reduce(lambda x, y: x * y, L)

print(product([1, 2, 3, 4, 5]))


# 练习3
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(string):
    powerX = 10
    powerY = 1
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}
    def fn(x, y):
        nonlocal powerX, powerY
        if y == '.':
            powerX = 1
            powerY = 0.1
            return x
        temp = x * powerX + y * powerY
        if powerY < 1:
            powerY *= 0.1
        return temp

    def char2num(s):
        return digits[s]
    return reduce(fn, map(char2num, string))
    # return list(map(char2num, string))

print(str2float('123.456'))
