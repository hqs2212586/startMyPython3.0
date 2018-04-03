
class Mymeta(type):   # 自定义元类，大多数属性依然是继承的type
    def __init__(self, class_name, class_bases, class_dic):
        # print(class_name)  # 类名：Chinese
        # print(class_bases)  # 基类：(<class 'object'>,)
        # print(class_dic)  # 类的名称空间：{'__module__': '__main__', '__qualname__': 'Chinese', 'country': 'China', '__init__': <function Chinese.__init__ at 0x101f201e0>, 'talk': <function Chinese.talk at 0x101f20378>}

        # 自订制控制类的行为
        if not class_name.istitle():  # istitle()判断首字母大写
            raise TypeError('类名的首字母必须大写')# 主动报错的关键字是raise

        if '__doc__' not in class_dic or not class_dic['__doc__'].strip():
            raise TypeError("必须有注释，且注释不能为空")

        super(Mymeta, self).__init__(class_name, class_bases, class_dic)  # 重用父类功能

#class Chinese(object, metaclass=type):  # metaclass元类，默认就是type
class Chinese(object, metaclass=Mymeta):  # 元类为Mymeta的类的创建可受人控制
    """
    中国人的类
    """
    country = 'China'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print('%s is talking' % self.name)


# Chinses = type(class_name, class_bases, class_dic)

