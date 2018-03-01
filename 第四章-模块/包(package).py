import sys

'''
# 绝对路径：
# 方式一：
# sys.path.append("/Users/huangqiushi/PycharmProjects/startMyPython3.0/学习/第三章-文件操作和函数/第四章-模块/packages/my_proj") # 路径不规范严谨
# ***入口程序所在的目录会加进sys.path，不管内部发生多少次调用，均以此为准***
# 因此需要在环境变量中添加路径。
from proj import settings

def sayhi():
    print('hello world!')
# 输出：in proj/settings.py


# 方式二：
import os
# print(dir())   # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'os', 'sayhi', 'sys']
# print(__file__)  # /Users/huangqiushi/PycharmProjects/startMyPython3.0/学习/第三章-文件操作和函数/第四章-模块/packages/my_proj/crm/views.py

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# # print(BASE_DIR)  # /Users/huangqiushi/PycharmProjects/startMyPython3.0/学习/第三章-文件操作和函数/第四章-模块/packages/my_proj
# sys.path.append(BASE_DIR)
# from proj import settings


# 方式三：
print(os.path.abspath(__file__))  # 绝对路径求法
sys.path.append(BASE_DIR)
'''

"""
相对路径   相对导入不能不相对到程序的根目录
"""
from . import models   # 常用
from ..proj import settings    # 不常用，容易返回到根目录
def sayhi():
    print('hello world!')
"""
文件夹被Python解释器视为package需要满足一下条件
    1、文件夹内必须有__init__.py文件，该文件可以为空，但必须存在该文件
    2、不能作为顶层模块来执行该文件夹中的py文件（即不能作为主函数的入口）
注意：虽然Python支持相对导入，但对模块间路径关系要求严格，处理不当容易出差，不建议经常使用
"""