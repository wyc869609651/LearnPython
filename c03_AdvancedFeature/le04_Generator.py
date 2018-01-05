# 生成器
# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 如果列表元素可以按照某种算法推算出来，那么我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建一个完整的list，从而节省大量的空间。在Python中，这种便循环边计算的机制，称为生成器：generator

# 要创建一个generator，有很多种方法，第一种方法很简单，只要把列表生成式的[]改成()，就创建了一个generator
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print(g)
# 创建L和g的区别仅在于外层的[]和()，L是一个list，而g是一个generator
# 我们可以直接打印出list的每一个元素，但是我们怎么打印出generator的每一个元素呢？
# 如果我们要一个一个打印出来，可以通过next()函数获得generator的下一个返回值：
print(next(g))
print(next(g))
print(next(g))
# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，
# 没有更多元素时，抛出StopIteration的错误
# 当然，不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generation也是一个可迭代对象
print('--------------------')
for n in g:
    print(n)
# print(next(g)):StopIteration
# 所以，我们创建一个generator后， 基本上永远不会调用next(),而是通过for循环来迭代它，并且不用关心StopIteration错误


# generator非常强大。如果推算的算法比较复杂，用类似生成式的for循环无法实现的时候，还可以用函数实现
# 斐波拉契数列（Fibonacci）
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


fib(10)
# 仔细观察，可以看出，fib函数实际上是定义了一个斐波拉契数列的推算规则，可以从第一个元素开始，
# 推算出后续的任意元素，这种逻辑其实非常类似generator。
# 也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改成yield b就行了


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
# 这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，
# 而是一个generator：
f = fib(6)
print(f)

# 这里最难理解的就是generator和函数的执行流程不一样。函数一顺序执行，遇到return语句或者最后一行语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

# 举个简单例子，定义一个generator，一次返回数字1， 3， 5：
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5
# 调用该generator时，首先要生成一个generator对象，然后next()函数不断获得下一个返回值：
o = odd()
print(next(o))
print(next(o))
print(next(o))
# print(next(o))
# 可以看到，odd不是一个普通函数，而是generator，在执行过程中，遇到yield就中断，下次又继续执行。
# 执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错。
# 回到fib的例子，我们在循环过程中不断调用yield，就会不断中断。当然，要给循环设置一个退出条件，
# 不然就会产生一个无限数列出来
# 同样，把函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代
for n in fib(6):
    print(n)
# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator retur value:', e.value)
        break


# Homework:杨辉三角
def triangles():
    oldList = newList = [1]
    while True:
        yield newList
        newList = [1]
        for i in range(len(oldList)-1):
            newList.append(oldList[i]+oldList[i+1])
        newList.append(1)
        oldList = newList

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
