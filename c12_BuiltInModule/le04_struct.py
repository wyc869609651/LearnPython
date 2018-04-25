# struct
# 准确地讲，Python没有专门处理字节的数据类型。但由于b'str'可以表示字节，所以，
# 字节数组＝二进制str。而在C语言中，我们可以很方便地用struct、union来处理字节，
# 以及字节和int，float的转换。

# 在Python中，比方说要把一个32位无符号整数变成字节，也就是4个长度的bytes，
# 你得配合位运算符这么写：
n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = n & 0xff
bs = bytes([b1, b2, b3, b4])
print(bs)
# 非常麻烦。如果换成浮点数就无能为力了。

# 好在Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。
# struct的pack函数把任意数据类型变成bytes：
import struct
print(struct.pack('>I', 10240099))
# pack的第一个参数时处理指令，'>I'的意思是：
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
# 后面的参数个数要和处理指令一致。
# unpack把bytes变成相应的数据类型：
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))
# 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
# 所以，尽管Python不适合编写底层操作字节流的代码，但在对性能要求不高的地方，利用struct就方便多了。



