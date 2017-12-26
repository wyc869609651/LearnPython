# 调用函数
help(abs)
print(abs(-100))
print(max(1, 23, -5, 10))

# 数据类型转换
# python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换成整数
print(int('123'))
print(int(12.34))  # int('12.34'):ValueError
print(float('12.34'))
print(str(1.23))
print(bool(1))  # 0：False; 非零：True
print(bool(''))  # 空字符：False; 非空字符:True

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了个“别名”
a = abs
print(a(-1))

# hex()函数把一个整数转换成十六进制表示的字符串
print(hex(255))
print(bin(255))
print(hex(1000))
print(bin(1000))
