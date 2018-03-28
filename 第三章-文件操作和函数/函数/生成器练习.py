def a(x,y):
    return x + y

def b():
    for i in range(12):
        yield i


c = b()
print(c)
for j in [1, 2, 3, 4]:
    c = (a(j, i) for i in c)
print(list(c))
'''
生成器表达式在没有被next的时候它只是一个表达式，只是一个表达式，不是具体的值
当for j in [1,2,3,4]运行完后，j的值就为4了，这个题可以写成以下这种
'''

# 上述过程的解析：
def a(x, y):
    return x + y

def b():
    for i in range(12):
        yield i


c = b()
j=1   # 第一次循环j=1
c = (a(i, j) for i in c)   # c = [a(i,j), a(i,j)...]
j=2   # 第二次循环j=2
c = (a(i, j) for i in c)   # c = [a(a(i,j),j), a(a(i,j),j)...]
j=3   # 第三次循环j=1
c = (a(i, j) for i in c)   # c = [a(a(a(i,j),j),j), a(a(a(i,j),j),j)...]
j=4
c = (a(i, j) for i in c)
print(list(c))             # 循环的时候都不赋值，最后使用的时候才赋值

