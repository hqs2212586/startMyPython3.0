# shelve模块是一个简单的k,v将内存数据通过文件持久化的模块，可以持久化任何pickle可支持的python数据格式
import shelve
# f = shelve.open('shelve_test')  # 打开一个文件
#
# names = ["alex","rain","test"]
# info = {'name':'alex','age':22}
#
# f["names"] = names # 持久化列表
# f["info_dic"] = info
#
# f.close()


d = shelve.open('shelve_test')  # 打开一个文件

print(d['names'])
print(d['info_dic'])
print(d)