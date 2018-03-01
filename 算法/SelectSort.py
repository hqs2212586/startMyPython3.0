# 选择排序（Selection sort）
# 每趟从待排序的数据元素中选出最小（或最大）的一个元素，顺序放在已排好序列最后。

data_set = [9,1,22,31,45,3,6,2,11]

smallest_num_index = 0 #初始化列表最小值，默认为第一个

loop_count = 0
for x in range(len(data_set)):
    for y in range(x,len(data_set)):
        #当前值比之前选出来的最小值要小，将他换为最小值
        if data_set[y] < data_set[smallest_num_index]:
            smallest_num_index = y
        loop_count +=1
    else:
        print("smallest num is ", data_set[smallest_num_index])
        tmp = data_set[smallest_num_index]
        data_set[smallest_num_index] = data_set[x]
        data_set[x] = tmp

    print(data_set)
    print("loop times", loop_count)

