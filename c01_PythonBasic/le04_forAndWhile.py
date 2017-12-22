# 循环
# for...in循环，依次把list或tuple中的每一元素迭代出来
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
# range()函数：可以生成一个整数序列
sum = 0
for i in range(0, 100, 2):
    sum += i
print(sum)

# while循环，只要条件满足，就不断循环，条件不满足时退出循环。
sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print(sum)

# break:在循环中，break语句可以提前退出循环。
# continue:在循环过程中，也可以通过continue语句，跳过当前循环，直接进入下次循环
