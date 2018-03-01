
"""
序列化：序列化是指把内存里的数据类型转变成字符串，
       以使其能存储到硬盘或通过网络传输到远程，因为硬盘或网络传输时只能接受bytes

用于序列化的两个模块：
    json，用于字符串 和 python数据类型间进行转换
    pickle，用于python特有的类型 和 python的数据类型间进行转换

Json模块提供了四个功能：dumps、dump、loads、load
pickle模块提供了四个功能：dumps、dump、loads、load
"""
"""
# 把内存数据转成字符，叫做序列化
data = {
    'roles':[
        {'role':'monster','type':'pig'},
        {'role':'hero','type':'关羽'}
    ]
}

f = open("game_status","w")
# f.write(data)   # 写入失败，write只能接收字符串或者是bytes
f.write(str(data))  # 内容写入文件中
"""

"""
# 把字符转成内存数据类型，叫做反序列化
f = open("game_status","r")
d = f.read()
d = eval(d)
print(d['roles'])
"""


"""
json支持得数据类型：str,int,tuple,list,dict
pickle支持Python里的所有数据类型，但只能在python里使用。（其他语言的格式无法适配）
"""