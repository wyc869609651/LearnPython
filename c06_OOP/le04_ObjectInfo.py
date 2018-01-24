# 获取对象信息
# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？

# 使用type()
# 首先，我们来判断对象类型，使用type()函数：
# 基本类型都可以用type()判断：
print(type(123))
print(type('abc'))
print(type(None))
# 如果一个变量指向函数或者类，也可以用type()判断：
print(type(abs))
class Animal(object):
    pass
a = Animal()
print(type(a))

# 但是type()函数返回的是什么类型呢？它返回对应的Class类型。如果我们要在if语句中判断，
# 就需要比较两个变量的type类型是否相同：
print(type(123) == type(456))
print(type(123) == int)
print(type('abc') == type('123'))
print(type('abc') == str)
print(type('abc') == type(123))
# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用
# types模块中的定义的常量：
import types
def fn():
    pass
print('---------- 1 ----------')
print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)


# 使用isinstance()
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class类型，可以使用isinstance()函数。

# 我们回顾上次的例子，如果继承关系是：
# object --> Animal --> Dog --> Husky
class Dog(Animal):
    pass
class Husky(Dog):
    pass
# 那么，isinstance()就可以告诉我们，一个对象是否是某种类型。先创建三种类型的对象：
a = Animal()
d = Dog()
h = Husky()
# 然后，判断：
print('--------- 2 --------')
print(isinstance(h, Husky))
# 没有问题，因为h变量指向的就是Husky对象。
# 在判断：
print(isinstance(h, Dog))
# h虽然自身是Husky类型，但由于Husky是从Dog继承下来的，所以，h也是还是Dog类型。换句话说，
# isinstance()判断的是一个对象是否该类型本身，或者位于该类型的父继承链上。
# 因此，我们可以确信，h还是Animal类型：
print(isinstance(h, Animal))

# 同理，实际类型是Dog的d也是Animal类型：
print(isinstance(d, Dog) and isinstance(d, Animal))
# 但是， d不是Husky类型：
print(isinstance(d, Husky))

# 能用type()判断的基本类型也可以用isinstance()判断：
print('---------- 3 -----------')
print(isinstance('abc', str))
print(isinstance(123, int))
print(isinstance(b'acd', bytes))

# 并且可以以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
print('-------- 4 ---------')
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
