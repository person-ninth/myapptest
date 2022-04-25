#迭代法最重要的是可以写出迭代式，用循环或者递归实现
a, b = 1, 1
c = a + b
x = int(input("请输入月份"))


def tuzi(a, b, c, x):#迭代式当月的兔子数等于前两个月的兔子数相加
    c = a + b
    a = b
    b = c
    if x == 3:
        print("数量为{1:d}".format(x, c))
    else:
        return tuzi(a, b, c, x-1)


print("兔子第{0:d}个月的".format(x), end='')
tuzi(a, b, c, x)
