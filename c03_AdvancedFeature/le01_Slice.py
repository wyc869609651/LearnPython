# 切片：Slice
# 切片是指取一个list或tuple的部分元素
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0, 1，2
# 如果第一个索引是0，还可以省略
print(L[:3])
# 类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片。
# 倒数第一个元素的索引是-1
print(L[-2:])
print(L[-2:-1])
# L[:]可以原样复制一个tuple
print(L[:])

# tuple也是一种list,唯一的区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
# 字符串'xxx'也可以看成是一种list,每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串。
str = 'ABCDEFG'
print(str[:3])
print(str[::2])

