# 冒泡排序（Bubble Sort）
# 它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。

data_set = [ 9,1,22,31,45,3,6,2,11 ]

loop_count = 0
for x in range(len(data_set)):
    # -1是因为每次对比的都是i 与i+1，不减1，最后一次对比会超出
    for y in range(len(data_set) - x -1):
        if data_set[y] > data_set[y+1]:
            tmp = data_set[y]
            data_set[y] = data_set[y+1]
            data_set[y+1] = tmp
        loop_count +=1
    print(data_set)


print(data_set)
print("loop times",loop_count)

