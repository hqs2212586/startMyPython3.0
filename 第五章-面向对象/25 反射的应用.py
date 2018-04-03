# 应用一：实现接受用户的输入来触发对象下相应的方法
# class Service:
#     def run(self):
#         while True:
#             cmd = input('>>: ').strip()
#             if hasattr(self, cmd):   # 判断有没有cmd
#                 func = getattr(self, cmd)  # get到cmd属性
#                 func()  # 方法调用
#
#     def get(self):
#         print('get......')
#
#     def put(self):
#         print('put......')
#
#
# obj = Service()
# obj.run()
"""
>>: ssad
>>: get
get......
>>: put
put......
"""

# 程序升级，支持get a.txt
class Service:
    def run(self):
        while True:
            inp = input('>>: ').strip()  # cmd='get a.txt'
            cmds = inp.split()  # cmd,args=['get','a.txt']

            if hasattr(self, cmds[0]):
                func = getattr(self, cmds[0])
                func(cmds)


    def get(self, cmds):
        print('get......', cmds)

    def put(self, cmds):
        print('put......', cmds)


obj = Service()
obj.run()
"""
>>: get a.txt
get...... ['get', 'a.txt']
>>: put a.txt
put...... ['put', 'a.txt']
>>: get
get...... ['get']
>>: put
put...... ['put']
"""