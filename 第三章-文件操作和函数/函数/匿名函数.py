
'''
匿名函数作用：
    1、节省代码量
    2、看起来比较高级
'''
'''
示例一：
def calc(x,y):
    return x*y
# 将上述一般函数改写为匿名函数
lambda x,y:x*y
'''
func = lambda x,y:x*y    # 声明一个匿名函数并赋值给func
print(func(3,8))       # 输出结果为24


'''
示例二：
将复杂函数改写为匿名函数
def calc(x,y):
    if x < y:
        return x*y
    else:
        return x/y
print(calc(16,8))
将上述函数转化为匿名函数，匿名函数支持得最复杂的运算就是三元运算。
'''
func1 = lambda x,y: x*y if x < y else x/y     # 转换为三元运算形式的匿名函数
print(func1(16,8))


'''
    匿名函数运用
'''
data = list(range(10))
print(data)
'''
# 方法一：
for index,i in enumerate(data):
    data[index] = i*i
print(data)

# 方法二：
def f2(n):
    return n*n
print(list(map(f2,data)))
'''
# 方法三：
print(list(map(lambda x:x*x,data)))   # map函数和匿名函数运用，用一次就不用了因此无须定义函数