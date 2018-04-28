
# configparser 此模块用于生成和修改常见配置文档

import configparser

conf = configparser.ConfigParser()  # 准备去处理文件

conf.read("conf.ini")
print(conf.sections())
print(conf.default_section)

print(list(conf["bitbucket.org"].keys()))
# 输出：['user', 'serveraliveinterval', 'compression', 'compressionlevel', 'forwardx11']


print(conf.has_section('topsercret.server.com'))
for k in conf["bitbucket.org"]:
    print(k)  # 每个节点都会默认有default值
