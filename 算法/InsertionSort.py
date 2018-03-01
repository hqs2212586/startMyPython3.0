# 插入排序(Inertion Sort)
# 列表分为2部分，左边是排序好的，右边为未排序的。
# 循环列表，每次将一个待排序记录按关键字大小插入前面已排好子序列中，直到全插入完。

source = [92,77,67,8,6,84,55,85,42,67]

for index in range(1,len(source)):
    #先记下每次大循环走到第几个元素的值
    current_val = source[index]
    position = index

    #当前元素的左边紧靠元素比它大，左边元素一一右移一位，给当前这个值插入到左边挪一位
    while position > 0 and source[position-1] > current_val:
        # 把左边的一个元素右移一位
        source[position]= source [position-1]
        # 还要继续左移至此元素放到排序好的列表的适当位置
        position -= 1
    #找到左边排序好列表不小于current_val元素位置，并放入这里
    source[position] =  current_val
    print(source)