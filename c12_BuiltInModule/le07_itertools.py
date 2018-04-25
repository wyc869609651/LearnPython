# itertools
# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
# 首先，我们看看itertools提供的几个“无限”迭代器：
import itertools
natuals = itertools.count(1)
# for n in natuals:
#     print(n)
# 因为count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，
# 只能按Ctrl+C退出。

# cycle()会把传入的一个序列无限重复下去：
cs = itertools.cycle('ABC')  # 注意字符串也是序列的一种
# for c in cs:
#     print(c)
# 同样停不下来。

# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
print('---------repeat---------')
ns = itertools.repeat('ABC', 3)
for n in ns:
    print(n)

# 无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限
# 个元素生成出来，事实上也不可能在内存中创建无限多个元素。

# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个
# 有限的序列：
print('---------takewhile---------')
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))
# itertools提供的几个迭代器操作函数更加有用：

# chain()
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
print('---------chain---------')
for c in itertools.chain('ABC', 'XYZ'):
    print(c)

# groupby()
print('---------groupby---------')
# groupby()把迭代器中相邻的重复元素挑选出来放在一起：
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))
# 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回值相等，这两个元素就被
# 认为是在一组的，而函数返回值作为组的key。如果我们要忽略大小写分组，就可以让元素'a'和
# 'A'都返回相同的key:
for key, group in itertools.groupby('AaaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))


# 练习
# 计算圆周率可以根据公式：
# 利用Python提供的itertools模块，我们来计算这个序列的前N项和：
import  itertools
def pi(N):
    # 计算pi的值
    # step1:创建一个奇数序列：1, 3, 5, 7, 9, ...
    ns = itertools.count(1, 2)
    odds = itertools.takewhile(lambda x: x % 2 == 1, ns)
    # step2:取该序列的前N项：1, 3, 5, 7, 9, ..., 2*N-1.
    odds = itertools.takewhile(lambda x: x <= 2*N-1, odds)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    # step 4: 求和:
    i = 0
    num = 0
    for x in odds:
        num += ((-1)**i)*4/x
        i += 1
    return num

print(pi(100))
