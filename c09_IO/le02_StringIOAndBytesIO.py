# StringIO
# 很多时候，数据读写不一定是文件，也可以在内存中读写。
# StringIO故名思义就是在内存中读写str
# 要把str写入StringIO，我们需要先创建一个StringIO，然后像文件一样写入即可：
from io import StringIO
f = StringIO()
f.write('Hello')
f.write(' ')
f.write('world!')
print(f.getvalue())
# getvalue()方法用于获得写入后的str。
# 要读取StringIO，可以用一个str初始化StringIO，然后，像文件一样读取：
f = StringIO('Hello!\nHi!\nGoodBye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())


# BytesIO
# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
# 请注意，写入的不是str，而是经过UTF-8编码的bytes。
# StringIO类似，可以用一个bytes初始化BytesIO，然后像文件一样读取：
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())


# 小结
# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。

