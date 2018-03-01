# 函数生成器send方法
def range2(n):

    count = 0
    while count < n:
        print('count', count)
        count += 1
        sign = yield count
        # yield count  # 执行结束就会抛出StopIteration的报错
        print("---sign", sign)
    return 3333  # 函数中有yield时就无法执行到return了

new_range = range2(3)  # 0，1，2

n1 = next(new_range)

print(new_range)

new_range.send("stop")
# send方法
# 1.唤醒并继续执行
# 2.发送一个信息到生成器内部
