# 排序算法:sorted
# 排序也是在程序中经常用到的算法。无论用的是冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
# 如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，
# 因此，比较的过程必须通过函数抽象出来。

# Python内置的sorted()函数就可以对list进行排序：
print(sorted([36, 5, -12, 9, -21]))

# 此外，sorted()函数也是一个高阶函数，他还可以接收一个key函数来实现自定义的排序，例如按绝对值的大小进行排序
print(sorted([36, 5, -12, 9, -21], key=abs))
# key指定的函数将作用于list的每一个元素上，并根据key函数的返回结果进行比较。

# 我们在看一个字符串排序的例子：
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。

# 现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，
# 只要我们能用一个key函数把字符串映射为忽略大小写排序即可。忽略大小写来比较两个字符串，
# 实际上就是先把字符串都变成大写（或者都变成小写），再比较。
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

# 从上述例子可以看出，高阶函数的抽象能力是非常强大的，而且，核心代码可以保持得非常整洁。

# 小结
# sorted()也是要给高阶函数。用sorted()排序的关键在于实现一个映射函数。

# 练习
# 假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序
def by_name(t):
    return t[0]

print(sorted(L, key=by_name))
# 再按成绩高低排序
def by_score(t):
    return t[1]

print(sorted(L, key=by_score))
