
import pickle

d = {'name':'alex','age':22}
# l = [1,2,3,4,'rain']
pk = open("data.pkl","wb")  # 针对bytes内容必须配置为wb模式
#
# print(pickle.dumps(d))  # b'\x80\x03}q\x00(X\x04\x00\x....  bytes类型
pickle.dump(d,pk)
"""
data.pkl文件内容：�}q (X   nameqX   alexqX   ageqKu.
文件格式不可直接读。
"""



# f = open("data.pkl","rb")
# d = pickle.load(f)
# print(d)
"""
输出：{'name': 'alex', 'age': 22}
"""


def sayhi():
    print('dddddd')

print(pickle.dumps(sayhi))
"""
执行不报错，说明pickle可以支持函数序列化
b'\x80\x03c__main__\nsayhi\nq\x00.'
"""

user_dic = {
                'username': 'alex',
                'password': 'asdadasdadad12131312'
            }
user_dumps = pickle.dumps(user_dic)
print(user_dumps)
user_loads = pickle.loads(user_dumps)
print(user_loads)