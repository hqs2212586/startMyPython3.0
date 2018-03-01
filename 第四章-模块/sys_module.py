# sys模块

import sys

sys.argv   # 命令行参数List，第一个元素是程序本身路径
"""
vi /Users/huangqiushi/PycharmProjects/checkServer/test_new.py
import sys
print(sys.argv)

python test_new.py run web  # run web 为脚本参数
输出：['test_new.py', 'run', 'web']
"""
# sys.exit()  # 退出程序，正常退出时exit(0)
"""
vi /Users/huangqiushi/PycharmProjects/checkServer/test_new.py
import sys
print(sys.argv)
sys.exit('bye')
print(333)    # 后面的语句不执行

python test_new.py run web
输出：['test_new.py', 'run', 'web']
      bye
"""

sys.version  # python解释程序的版本信息
"""
>>> sys.version
'3.6.3 |Anaconda, Inc.| (default, Oct  6 2017, 12:04:38) \n[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)]'
"""

sys.maxsize  # 最大的int值  Python2中为sys.maxint
"""
>>> sys.maxsize
9223372036854775807
"""

sys.path   # 模块的搜索路径，初始化时使用PythonPATH环境变量的值

sys.platform
"""
>>> sys.platform
'darwin'  # mac发行版
"""

sys.stdout
"""
>>> sys.stdout  # 将屏幕作为一个文件
<_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'>
"""
sys.stdout.write()  # 标准输出
"""
>>> sys.stdout.write('hey!good morning!')
hey!good morning!17
"""
sys.stdin  # 标准输入  往屏幕输入东西
sys.stdin.read()  # 一直读
sys.stdin.readline()  # 读一行

sys.getrecursionlimit()  # 获取最大递归层数  默认是1000（0-999）
sys.setrecursionlimit(1200)  # 设置最大递归层数

sys.getdefaultencoding()  # 获取解释器默认编码
sys.getfilesystemencoding()   # 获取内存数据存到文件里的默认编码
"""
>>> sys.getdefaultencoding()
'utf-8'
>>> sys.getfilesystemencoding()
'utf-8'
"""