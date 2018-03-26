"""
    递归定义：在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
    递归特性：
        1、必须有一个明确的结束条件
        2、每次进入更深一层递归时，问题规模相比上次递归都应有所减少
        3、递归效率不高，递归层次过多会导致栈溢出（在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，
        栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以递归调用的次数过多，会导致栈溢出。）
"""

# 把10不断除2，直到不能除为止，打印每次结果
'''
方法一：
# 运用循环实现
n =10
while True:
    n = int(n/2)
    print(n)
    if n == 0 :
        break
'''

'''
方法二：
# 用函数改写
def calc(n):
    n = int(n/2)
    print(n)
    return n

r1 = calc(10)
r2 = calc(r1)
r3 = calc(r2)
print(r3)
'''

'''
# 方法三：
# 递归函数改写
# 递归用途：不知道问题什么时候解决的时候，可以选择使用递归
# 递归层次一般限制为1000层,用下述方法验证
import sys
print(sys.getrecursionlimit())   # 显示递归最大限制1000层

def calc(n):
    n = int(n/2)
    print(n)        # 一层层进入，并打印
    if n > 0:
        calc(n)             # 函数本身传入函数
    print(n)        # 一层层退出，并打印
calc(10)
# 输出5 2 1 0 0 1 2 5
# 一层层进入，一层层退出
'''

# 递归的返回值


def calc(n, count):
    print(n, count)
    if count < 5:
        return calc(n/2, count+1)   # 最后一层返回到倒数第二层执行该语句并返回
    else:
        return n  # 最后一层返回到上一层


res = calc(188, 1)
print('res', res)
