# 实例属性和类属性

# 由于Python是动态语言，根据类创建的实例可以绑定任意属性。
# 给实例绑定属性的方法是通过实例变量，或者通过self变量：
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90
# 但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，
# 归Student类所有：
class Student(object):
    name = 'Student'

# 当我们定义一个类属性后，这个属性归类所有，但类的所有实例都可以访问。来测试一下：
s = Student()
print(s.name)
print(Student.name)
s.name = 'Michael'
print(s.name)
print(Student.name)
del s.name  # 如果删除实例的name属性
print(s.name)  # 再次调用s.name属性，由于实例的name属性没有找到，类的name属性就显示出来了

# 从上面的例子可以看出，在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为形同的
# 名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，在使用相同的名称，访问到的将是类属性。


# 练习
# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class NewStudent(object):
    count = 0

    def __init__(self, name):
        self.name = name
        NewStudent.count += 1


# 小结
# 实例属性属于各个实例所有，互不干扰；
# 类属性属于类所有，所有实例共享一个属性；
# 不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。

