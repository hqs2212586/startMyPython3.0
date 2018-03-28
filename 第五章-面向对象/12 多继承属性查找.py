class A(object):
    def test(self):
        print('from A')

class B(A):
    def test(self):
        print('from B')

class C(A):
    def test(self):
        print('from C')

class D(B):
    def test(self):
        print('from D')

class E(C):
    def test(self):
        print('from E')

class F(D,E):
    # def test(self):
    #     print('from F')
    pass
f1=F()
f1.test()  # 寻找test方法

print(F.__mro__)  # 只有新式才有这个属性可以查看线性列表，经典类没有这个属性
"""
from F
(<class '__main__.F'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.E'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
"""

#新式类继承顺序:F->D->B->E->C->A  广度优先
#经典类继承顺序:F->D->B->A->E->C  深度优先
#python3中统一都是新式类
#pyhon2中才分新式类与经典类