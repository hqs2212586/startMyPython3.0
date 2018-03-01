iphone7 = {'alex','rain','jack','old_driver'}
iphone8 = {'alex','shanshan','jack','old_boy'}

# 交集
iphone7.intersection(iphone8)
# 交集
iphone7 & iphone8

# 差集
iphone7.difference(iphone8) # iphone7有iphone8没有的
# 差集
iphone7 - iphone8

# 并集(去重)
iphone7.union(iphone8)
# 并集
iphone8 | iphone7   # 管道符

# 对称差集（只买了iPhone7 or iphone8的人）
iphone8.symmetric_difference(iphone7)
# 对称差集
iphone7 ^ iphone8