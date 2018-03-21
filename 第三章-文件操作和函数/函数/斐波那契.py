# 用函数来写生成器，以斐波那契数列为例
# Fibonacci：除第一个和第二个数外，任意一个数可由前两个数相加得到
# 1,1,2,3,5,8,13,21,34,...
# 重点是赋值语句：a,b = b,a+b
#
# def fib(max):  # 用列表生成式写不出来，但是用函数打印却很容易
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)   # 每次打印b
#         a, b = b, a + b  # 0，1——>1，1——>1，2——>2，3
#         n = n + 1   # n用来计数，每次自加1
#     return 'done'
#
# fib(10)

# 生成器写斐波那契数据
def fib_g(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print('before yield')
        yield b   # yield 把函数的执行过程冻结在这一步，并且把b的值返回给外面的next()
        # print(b)
        a, b = b, a+b
        n = n + 1
    return 'done'
# f = fib_g(15)  # 将函数转换为生成器，有了yeild后，函数名(参数)根本不执行

# 生成器使用意义：可以将函数执行中的状态、数据返回到外部来
# next(f) # first time call next()


# data = fib_g(10)
# print(data)
#
# print(data.__next__())
# print(data.__next__())
# print("干点别的事")
# print(data.__next__())
# print(data.__next__())
# print(data.__next__())
# print(data.__next__())

# for n in fib_g(6):
#     print(n)

g = fib_g(6)
while True:
    try:
        x = next(g)
        print('g', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


