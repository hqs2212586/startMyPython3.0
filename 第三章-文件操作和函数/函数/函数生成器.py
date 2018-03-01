
def range2(n):

    count = 0
    while count < n:
        print('count',count)
        count += 1
        yield count  # 类似return,

print(range2(10))  # <generator object range2 at 0x101447200>
new_range = range2(10)

r1 = next(new_range)
print(r1)
r2 = next(new_range)
print(r2)
next(new_range)

new_range.__next__()  # next(new_range)的改写方式

'''
f = open("text.txt")
for i in f:   # 相当于一个生成器
    print(i)
'''