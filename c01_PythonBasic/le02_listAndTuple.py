# list
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[1])  # 第二个
print(classmates[-1])  # 倒数第一个
classmates.append('Adam')  # 往list中追加元素到末尾 append()
print(classmates)
classmates.insert(1, 'Jack')  # 把元素插入到指定位置 insert()
print(classmates)
classmates.pop()  # 删除list末尾元素 pop()
print(classmates)
classmates.pop(1)  # 删除指定位置的元素 pop(index)
print(classmates)
classmates[1] = 'Sarah'  # 把某个元素替换成别的元素，可以直接赋值给对应的索引位置
print(classmates)
# list里面的元素的数据类型也可以不同
diffList = ['python', 123, True, ['sap', 'java']]
print(len(diffList))
print(diffList[3][0])

# tuple
# 另一种有序列表叫元组：tuple。 tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates = ('Michael', 'Bob', 'Tracy')
# tuple中没有append(), insert()这样能改变tuple的方法
# 可以正常使用tuple[index]获取tuple中的值，但不可以赋值
# tuple的陷阱：当定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如
t = (1, 2)
print(t)
# 如果要定义一个空的tuple，可以写成（）；
# 但是如果要定义一个只有1个元素的tuple,需要这样写：
t = (1,)
print(t)
# 因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义。
# 因此，Python规定，这种情况下按小括号进行计算。
# 所以，只有一个元素的tuple定义时必须加一个逗号","，来消除歧义

# “可变的”tuple
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)  # ('a', 'b', ['X', 'Y'])
# tuple所谓的"不变"是说，tuple的每个元素的指向永远不变。但指向的对象本身是可以改变的
