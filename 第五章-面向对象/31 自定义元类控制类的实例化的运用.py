# 单例模式:参数一样的实例，不用申请新的内存空间给新的对象
# 实现方式一：
# class MySQL:
#     __instance = None   # 实例化后改为了__instance = obj1
#     def __init__(self):
#         self.host = '127.0.0.1'
#         self.port = 3306
#
#     @classmethod
#     def singleton(cls):
#         if not cls.__instance:
#             obj = cls()
#             cls.__instance = obj
#         return cls.__instance
#
#     def conn(self):
#         pass
#
#     def execute(self):
#         pass
#
# # obj1 = MySQL()
# # obj2 = MySQL()
# #
# # print(obj1)
# # print(obj2)
#
# obj1 = MySQL.singleton()
# obj2 = MySQL.singleton()
# obj3 = MySQL.singleton()
#
# print(obj1 is obj3)
"""
True
"""


# 实现方式二： 元类的方式
class Mymeta(type):
    def __init__(self, class_name, class_bases, class_dic):
        if not class_name.istitle():  # istitle()判断首字母大写
            raise TypeError('类名的首字母必须大写')  # 主动报错的关键字是raise

        if '__doc__' not in class_dic or not class_dic['__doc__'].strip():
            raise TypeError("必须有注释，且注释不能为空")

        super(Mymeta, self).__init__(class_name, class_bases, class_dic)  # 重用父类功能
        self.__instance = None


    def __call__(self, *args, **kwargs):  # obj = Chinese('egon',age=18)
        if not self.__instance:
            obj=object.__new__(self)  # self:Mysql
            self.__init__(obj)
            self.__instance=obj
        return self.__instance

class Mysql(object, metaclass=Mymeta):
    """
    mysql
    """
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 3306

    def conn(self):
        pass

    def execute(self):
        pass


obj1 = Mysql()
obj2 = Mysql()
obj3 = Mysql()

print(obj1 is obj2 is obj3)  # "True"
