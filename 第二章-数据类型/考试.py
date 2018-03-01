#
# name = " aleX"
# print(name.strip())
#
# print(name.upper())
#
# print(name.endswith("X"))
#
# print(name[:3])
#
# print(name[-2:])
#
# new_name = name[:-1]
# print(new_name)
#
#
# dict1 = {"Development":"开发小哥", "OP":"运维小哥", "Operate":"运营小仙女", "UI":"UI小仙女"}
#
# dict1["TEST"] = "测试人员"
#
# print(dict1)
#
# print(dict1.pop("OP"))
#
# print(dict1)
#
# dict1["UI"] = "asasdad"
#
# print(dict1)
#
# for i in dict1.values():
#     print(i)
#
# n = 2
# sum_r = 0
# while n < 101:
#     if n % 2 ==0:
#         sum_r = sum_r + n
#     else:
#         sum_r = sum_r - n
#     n += 1
# print(sum_r)


li = [1,3,2,7,6,23,41,24,33,85,56]

for i in range(0,len(li)):
    for j in range(i+1,len(li)):
        if li[i] > li[j]:
            li[i], li[j] = li[j], li[i]
    print(li)