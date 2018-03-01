
user_status = False
def login(func):
    def inner(*args,**kwargs):   # 添加参数eg.3p
        _username = "alex"
        _password = "abc!23"
        global user_status

        if user_status == False:
            username = input("user:")
            password = input("password:")
            if username == _username and password == _password:
                print("welcome login...")
                user_status = True
            else:
                print("wrong username or password!")
        else:
            print("wrong username or password!")
        if user_status:
            # func(args,kwargs)  # 这样写是固定两个参数
            func(*args,**kwargs)   # henan()  适配任意多个参数
    return inner # 加括号执行，不加括号返回内存地址

def home():
    print("首页".center(40,'-'))
def america():
    print("欧美专区".center(40,'-'))
'''
    运用非固定参数解决一个需要参数一个不需要参数等的问题
'''
@login
def japan():
    print("日韩专区".center(40,'-'))
@login  # henan = login(henan)
def henan(style):
    print("河南专区".center(40,'-'),style)

henan('3p')
japan()