# -*- conding:utf-8 -*-

# user = input("type your name please!")
# addr = input("where are you come from?")
# habbit = input("what is your habbit?")
#
# print("敬爱可爱的" + user + "，最喜欢在"+addr+"地方干"+habbit)


def work(n):
    count = 0
    while count < n:
        count += 1
        sign = yield count
        if not sign:
            yield count+2


new_range = work(4)
res = next(new_range)
print(res)
res1 = new_range.send(True)
print(res1)
res2 = new_range.send(False)
print(res2)