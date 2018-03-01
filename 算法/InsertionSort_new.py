# 插入排序(Inertion Sort)
# 列表分为2部分，左边是排序好的，右边为未排序的。
# 循环列表，每次将一个待排序记录按关键字大小插入前面已排好子序列中，直到全插入完。

data_set = [9,1,22,9,31,-5,45,3,6,2,11]
for i in range(len(data_set)):
    # position = i
    # 右边小于左边相邻的值
    while i > 0 and data_set[i] < data_set[i -1]:
        tmp = data_set[i]
        data_set[i] = data_set[i-1]
        data_set[i-1] = tmp
        i -= 1
    