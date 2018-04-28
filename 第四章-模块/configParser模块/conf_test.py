
# configparser 此模块用于生成和修改常见配置文档

import configparser

conf = configparser.ConfigParser()  # 准备去处理文件
conf.read('conf_test.ini')

# print(dir(conf))
# print(conf.options("group1"))
# print(conf['group1']["k2"])
# """
# ['k1', 'k2']
# v2
# """
#
# # 添加
# conf.add_section("group3")
# conf['group3']['name'] = 'hqs'
# conf['group3']['age'] = '22'  # 不能使用数字
#
# conf.write(open('conf_test_new.ini', "w"))  # 写入新文件

# # 删除
# # 删除某一项配置
# conf.remove_option('group1', "k2")
# conf.write(open("conf_test_new.ini", "w"))
# 删除某一整个章节
# conf.remove_section('group1')
# conf.write(open("conf_test2.ini", "w"))

print(conf.items('group1'))