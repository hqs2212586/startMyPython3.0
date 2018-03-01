
import json

# f = open("json_file","w",encoding="utf-8")
# d = {'name':'alex','age':22}
# l = [1,2,3,4,'rain']
# json.dump(d,f)
# json.dump(l,f)
# """
# 可以多次dump,文件内容如下：
# {"name": "alex", "age": 22}[1, 2, 3, 4, "rain"]
# """

f = open("json_file",'r',encoding="utf-8")
json.load(f) # JSONDecodeError,无法解析这两条数据
"""
因此每次都必须是dump一次，load一次
"""