# 定义函数
# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号：
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-99))
# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return

# ---------------------------空函数--------------------------
# 如果想定义一个什么事也不做的空函数，可以用pass语句：


def nop():
    pass
# pass可以用来作为占位符，比如现在还没有想好怎么写函数的代码，就可以先放
# 一个pass让代码能运行起来
# pass还可以用在其他语句里，比如
# if age >= 18:
#     pass
# 缺少了pass,代码运行就会有语法错误

# ------------------------参数检查-------------------------
# 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError
# 但是如果参数类型不对，Python解释器就无法帮我们检查。
# 我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。
# 参数类型检查可以用内置函数isinstance()实现：


def my_abs1(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# my_abs1('A')

# ---------------------------返回多个值-----------------------
import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi/6)
print(x, y)
# 但其实这是一种假象，Python函数返回的仍然是单一值：
r = move(100, 100, 60, math.pi/6)
print(r)
# 原来返回值是一个tuple!但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple,
# 按位置赋给对应的值。所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便


# --------------------作业-------------------
# 定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：ax² + bx + c = 0 的两个解


def quadratic(a, b, c):
    if not isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
        raise TypeError('bad operand type')
    if(b**2 - 4*a*c) < 0:
        print('此方程无解！')
        return
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    return x1, x2


print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))
