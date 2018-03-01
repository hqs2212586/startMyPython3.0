# 内置方法（Built-in Functions）
'''
abs()  # 取绝对值
dict() # 把数据转为字典
help() # 帮助
min()  # 找出最小值
max()  # 找出最大值
setattr()  #
bool() # 判断True or False(bool(0)、bool(Flase)、bool([]))
all()  # 可循环的数据集合每个元素bool()均为True；或者空列表也是True
any()  # 任意一个值是True即返回True
dir()  # 打印当前程序里的所有变量
hex()  # 转换为16进制数
slice()  # 提前定义切片规则
divmod()  # 传入两个变量a、b，得到a//b结果和余数a%b
sorted()  # 列表排序sorted(li)等同于li.sort()
'''
'''
d = {}
for i in range(20):
    d[i] = i - 50
d.items() # 字典转化为数组
sorted(d.items)
sorted(d.items(), key = lambda x:x[1])
sorted(d.items(), key = lambda x:x[1],reverse=True)
'''
ascii(2)  # 只能返回ascii码
enumerate([3,2,13,4])  # 返回列表的索引
input('dasd')
oct(10)  # 转八进制
# staticmethod()
bin(10)  # 转二进制

# eval()  # 字符串转代码（只能处理单行代码）（可以拿到返回值）
'''
f = "1+3/2"
eval(f)
# 输出结果：2.5

eval('print("hello world")')
# 输出结果：hello world
'''
# exec() # 字符串转代码（可以解析多行代码）（不能拿到返回值）
'''
code = "\nif 3>5:\n print('3 bigger than 5')\nelse:\n print('dddd')\n\n"
exec(code)
# 输出结果：dddd
'''
# eval和exec()返回值验证
code = '''
def foo():
    print('run foo')
    return 1234
foo()
'''
res = eval("1+3+3")
res2 = exec("1+3+3")
res3 = exec(code)
print('res',res,res2,res3)
# 输出结果：res 7 None None

open() # 文件打开
str()  # 转字符串
isinstance()
ord('a')  # 返回97，ascii码中'a'位置
chr(97)   # 返回'a',输入97位置返回ascii码对应字符
sum([1,4,5,-1,3,0])   # 计算列表求和



bytearray() # 将字符串转为bytearray，完成修改后，decode()后，可在原内存地址修改字符串
'''
>>> s = 'abcd路飞'
>>> s
'abcd路飞'
>>> s = s.encode('utf-8')
>>> s
b'abcd\xe8\xb7\xaf\xe9\xa3\x9e'
>>> s = bytearray(s)
>>> s
bytearray(b'abcd\xe8\xb7\xaf\xe9\xa3\x9e')
>>> s[4]
232
>>> s[4]=233
>>> s
bytearray(b'abcd\xe9\xb7\xaf\xe9\xa3\x9e')
>>> s.decode()
'abcd鷯飞'
>>> id(s)   # 修改内部元素，s指向的内存地址并不会改变
4352883880
'''



map(lambda x:x*x , [1,2,3,4,5])    # 根据提供的函数对指定序列做映射
'''
>>> list(map(lambda x:x*x , [1,2,3,4,5]))
[1, 4, 9, 16, 25]
'''
filter() # 将符合条件的值过滤出来
'''
>>> list(filter(lambda x: x>3, [1,2,3,4,5]))
[4, 5]
'''
import functools
functools.reduce()
'''
函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
    1、用传给reduce中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作
    2、得到的结果再与第三个数据用 function 函数运算，最后得到一个结果
functools.reduce(lambda x,y:x+y,[1,3,5,2444,221,2,4,7])   # 相加 2687
functools.reduce(lambda x,y:x*y,[1,3,5,2444,221,2,4,7])   # 相乘
functools.reduce(lambda x,y:x+y,[1,3,5,2444,221,2,4,7],3)  # 列表后面再加一个元素  2690
'''

pow(100,2) # 返回x的y次方，10000

callable()   # 查看函数是否可以调用，还可用于判断变量是否是函数

format()

frozenset()  # 不可变集合
'''
>>> s = {12,3,4,4}
>>> s.discard(3)
>>> s
{12,4}
>>> s = frozenset(s)
>>> s.   # 已经没有discard方法可以调用
'''

vars()  # 打印变量名和对应的值
locals()  # 打印函数的局部变量（一般在函数内运行）
globals() # 打印全局变量

repr()  # 显示形式变为字符串

zip()  # 可将两个数组一一对应组成元祖
'''
>>> a = [1,2,3,45,6]
>>> b = ['a','b','c']
>>> zip(a)
<zip object at 0x1034fe408>
>>> list(zip(a,b))
[(1, 'a'), (2, 'b'), (3, 'c')]
'''
compile() # 编译代码

complex() # 将一个数变为复数
'''
>>> complex(3,5)
(3,5j)
'''
round(1.2344434,2)  # 指定保留几位小数  输出1.23

# delattr, hasattr, getattr, setattr  # 面向对象中应用

hash()   # 把一个字符串变为一个数字

memoryview() # 大数据复制时内存映射
set()  # 把一个列表变为集合
'''
>>> set([12,5,1,7,9])
{1, 5, 7, 9, 12}
'''