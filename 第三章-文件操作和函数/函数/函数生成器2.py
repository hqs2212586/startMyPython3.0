# 函数生成器send方法
def range2(n):

    count = 0
    while count < n:
        print('count', count)
        count += 1
        sign = yield count
        if sign == 'stop':
            break
        print("---sign", sign)
    return 3333


new_range = range2(3)  # 0，1，2
n1 = next(new_range)
print(new_range)
new_range.send("stop")
# send方法
# 1.唤醒并继续执行
# 2.发送一个信息到生成器内部
