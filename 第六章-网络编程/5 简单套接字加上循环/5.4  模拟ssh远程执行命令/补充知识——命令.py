# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

# windows命令
# dir:查看某一个文件夹下的子文件名与子文件夹名
# ipconfig:查看本地网卡的ip信息
# tasklist:查看运行的进程

# linux命令
# ls
# ifconfig
# ps aux


# 执行系统命令
# import os
# cmd = os.popen('df -h')
# cmd = cmd.read()
# print(cmd)

import subprocess
obj = subprocess.Popen('dxxxs', shell=True,
                 stdout=subprocess.PIPE,  # stdout:正确结果;管道
                 stderr=subprocess.PIPE)   # stderr:错误结果;管道
"""
subprocess命令执行的结果就是bytes，无需转变格式就可以给客户端、服务端使用
"""

print(obj)
print('stdout 1---->: ', obj.stdout.read().decode('utf-8'))  # 正确管道内容

print('stderr 1---->: ', obj.stderr.read().decode('utf-8'))  # 错误管道内容

"""
<subprocess.Popen object at 0x10401ada0>
stdout 1---->:  
stderr 1---->:  /bin/sh: dxxxs: command not found
"""