# 使用__slots__
# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，
# 这就是动态语言的灵活性。先定义class：
class Student(object):
    pass

# 然后，尝试给实例绑定一个属性：
s = Student()
s.name = 'Michael'  # 动态给实例绑定一个属性
print(s.name)

# 还可以尝试给实例绑定一个方法：
def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(25)  # 调用实例方法
print(s.age)

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
s2 = Student()
# s2.set_age

# 为了给所有实例都绑定方法，可以给class绑定方法：

def set_score(self, score):
    self.score = score

Student.set_score = set_score

# 给class绑定方法后，所有实例均可调用：
s.set_score(100)
print(s.score)
s2.set_score(99)
print(s2.score)
# 通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中
# 动态的给class加上功能，这在静态语言中很难实现。

# 使用__slots__
#
