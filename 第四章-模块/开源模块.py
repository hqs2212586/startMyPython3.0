
"""
开源模块安装、使用
    https://pypi.python.org/pypi是Python的开源模块库。
    只要注册一个账号就可以往这个平台上传你的模块

方法一：
    下载网站上的安装包到本地，(PyTyrion为例)
    编译源码：python setup.py build
    安装源码：python setup.py install

方法二：
    pip3 install PyTyrion       # 安装模块
    pip3 uninstall PyTyrion     # 删除模块
"""

"""
pip默认连接国外的Python官方服务器下载，使用国内豆瓣源，数据会定期同步国外官网
pip install -i http://pypi.douban.com/simple/ paramiko --trusted-host pypi.douban.com
"""
import paramiko

ssh = paramiko.SSHClient
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.188',22,'hqs','123')

stdin, stdout, stderr = ssh.exec_command('df')
print(stdout.read())
ssh.close()
# 以上代码通过用户名和密码连接服务器
