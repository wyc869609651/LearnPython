print('----------------------默认参数-------------------')
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# 这样我们调用power(5)时，相当于调用power(5, 2)
print(power(5))
print(power(5, 3))


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
# 有多个默认参数时，调用的时候，既可以按顺序提供默认参数，比如调用enroll('Bob', 'M', 7),
# 意思是，只有city参数使用默认参数；
# 也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。
# 比如：enroll('Adam', 'M', city='Tianjin')


# 默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，演示如下：
def add_end(L=[]):
    L.append('END')
    return L


print(add_end())  # ['END']
print(add_end())  # ['END', 'END']
# 原因：Python函数在定义的时候，默认参数L的值就被计算出来了，即[],
# 因为默认参数L也是一个变量，它指向对象[],每次调用该函数，如果改变了L的内容，
# 则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了


# 定义默认参数要牢记一点：默认参数必须指向不变对象！！！
# 要修改上面的例子，我们可以用None这个不变对象实现：
def add_end1(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print('----------------------可变参数------------------------')
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加一个*号。
# 在函数内容参数接收到的是一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 3))
print(calc())
# 如果已经有一个list或者tuple,要调用一个可变参数怎么办？可以这样做
nums = [1, 2, 3]
print(calc(nums[0], nums[1], nums[2]))
# print(calc(nums)):TypeError
# 这种方式当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，
# 把list或tuple变成可变参数传进去
print(calc(*nums))


print('-----------------关键字参数---------------')
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键自参数允许你传入0个或任意个含参数名的参数，这些关键自参数在函数内部自动组装为一个dict。‘
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other', kw)
# 函数person除了必选参数name和age外，还接收关键字参数kw。


person('Michael', 30)
person('Adam', 45, gender='M', job='Engineer')
# 和可变参数类似，也可以先组装出一个dict,然后，把该dict转换为关键字参数穿进去：
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
# 当然，上面复杂的调用可以用简化的写法：
person('Jack', 24, **extra)
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数**kw参数，kw将获得一个dict,
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra


print('-------------------命名关键字参数--------------------')
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。
# 至于到底传入了哪些，就需要在函数内容通过kw检查。
# 仍以person()函数为例，我们检查是否有city和job参数：
def person1(name, age, **kw):
    if 'city' in kw:
        pass  # 有city参数
    if 'job' in kw:
        pass  # 有job参数
    print('name:', name, 'age:', age, 'other:', kw)


# 但是调用者仍可以传入不受限制的关键字参数：
person1('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


# 如果要限制关键字参数的名字，就可以用命名关键字参数；
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person2(name, age, *, city, job):
    print(name, age, city, job)


person2('Jack', 24, city='Beijing', job='Engineer')


# 如果函数定义中已经有了可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*号了
def person3(name, age, *args, city, job):
    print(name, age, args, city, job)


# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将会报错
# person3('Jack', '24', 'Beijing', 'Engineer')

# 命名关键字参数可以有缺省值，从而简化调用
def person4(name, age, *, city='Beijing', job):
    print(name, age, city, job)


# 由于命名关键字参数city具有默认值，调用时，可以不传入city参数：
person4('Jack', 24, job='Engineer')


# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用他，无论他的参数试是怎么定义的


# homework
def product(*nums):
    result = 1
    for n in nums:
        result *= n
    return result


print(product(4, 5, 6))
