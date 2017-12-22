# 编码
print(ord("A"))
print(ord("中"))
print(chr(66))
print(chr(25991))
print(len('ABC'))
print(len('中文'))
print(len('中文'.encode('utf-8')))

# 格式化输出
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print('growth rate: %d %%' % 7)
r = 85/72*100
print('score growth rate: %.1f%%' % r)
