# 文件操作分为读、写、修改

# 以什么模式存文件，就以什么模式编码打开文件
# 示例一：r是文本只读模式
f = open(file='D:/工作／兼职联系信息.txt',mode='r',encoding='utf-8')  # 绝对路径访问
data = f.read()
f.close()

# 示例二：# rb：二进制只读模式，无法指定encoding,因为在该模式下数据读到内存里直接是bytes格式，如要查看内容还需手动decode
f = open(file='兼职联系信息.txt', mode='rb')

# 文件智能检查————可解决不清除要处理文件是什么编码的问题
import chardet   # chardet需要用pip安装第三方工具包（pip3 install chardet）
'''
huangqiushi@MacBook-Air:~$ pip3 install chardet
Collecting chardet
  Using cached chardet-3.0.4-py2.py3-none-any.whl
Installing collected packages: chardet
Successfully installed chardet-3.0.4
'''
f = open('兼职联系信息.txt',mode='rb')
data = f.read()
f.close()
result = chardet.detect(data)  # 检查文件编码格式
print(result)  # 输出如下结果
# {'encoding': 'utf-8', 'confidence': 0.87625, 'language': ''}
data.decode("utf-8")   # 解码

# 修改编码后查看文件信息
f = open('兼职联系信息.txt',mode='r',encoding='utf-8')
data = f.read()
print(data)
