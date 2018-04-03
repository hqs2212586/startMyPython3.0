# 参考地址：http://www.cnblogs.com/linhaifeng/articles/6204014.html

# item系列
class Foo:
    def __init__(self, name):
        self.name = name

    def __getitem__(self, item):
        # print('getitem...')
        #print(item)

        return self.__dict__.get(item)  # 字典get方法有则取值，无也不会报错

    def __setitem__(self, key, value):
        # print('setitem...')
        # print(key,value)
        self.__dict__[key] = value

    def __delitem__(self, key):
        # print('delitem...')
        # print(key)
        # self.__dict__.pop(key)
        del self.__dict__[key]

obj = Foo('egon')


# 1、查看属性
# obj.属性名
# item系列就是为了把对象模拟成像字典一样，就可以像字典一样访问
obj['name']   # 以这种形式完成 obj.name取值的效果
"""
getitem...
name
"""
print(obj['name'])


# 2、设置属性
# obj.sex = 'male'
obj['sex'] = 'male'

print(obj.__dict__)
print(obj.sex)

# 3、删除属性
# del obj.name
del obj['name']
print(obj.__dict__)
"""
{'sex': 'male'}
"""