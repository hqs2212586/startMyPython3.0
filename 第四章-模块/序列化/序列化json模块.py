# json，用于字符串 和 python数据类型间进行转换
# Json模块提供了四个功能：dumps、dump、loads、load

import json
data = {
    'roles':[
        {'role':'monster','type':'pig'},
        {'role':'hero','type':'关羽'}
    ]
}

"""
只是把数据类型转成字符串存到内存里的意义？  json.dumps   json.loads
    1、把你的内存数据 通过网络（bytes） 共享给远程其他人
    2、定义了不同语言之间的交互规则
            1.纯文本，缺点：不能共享复杂的数据类型
            2.xml，缺点：占空间大
            3.json，简单，可读性好
"""
d = json.dumps(data)  # 仅转为字符串，可以存入硬盘
print(d,type(d))
# 输出：{"roles": [{"role": "monster", "type": "pig"}, {"role": "hero", "type": "\u5173\u7fbd"}]} <class 'str'>


f = open("test.json","w")  # 创建文件对象
d1 = json.dump(data,f)  # dump不仅将数据变为字符串还直接写入文件，但是只能存入文件对象中


d2 = json.loads(d)  # 仅把字符串转为相应的数据类型
print(d2['roles'],type(d2))
# 输出：[{'role': 'monster', 'type': 'pig'}, {'role': 'hero', 'type': '关羽'}] <class 'dict'>
"""
从文件中读入：
f = open("test.json","r")
data = json.load(f)
print(data['roles'])
"""

