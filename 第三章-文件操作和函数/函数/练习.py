
user_db = {
    'hqs':'123',
    'susiff':'123',
    'guangfa':'123'
}

with open('db.txt', 'w', encoding='utf-8') as f:
    f.write(str(user_db))
login_db = {'user': None, 'status': False}
db_path = r'db.txt'

def login(func):
    def inner(*args,**kwargs):
        if login_db['user'] and login_db['status']:
            res = func(*args, **kwargs)
            return res
        user = input('input user:')
        passwd = input('input passwd:')
        with open(db_path, 'r', encoding='utf-8') as f:
            user_db2 = eval(f.read())
        if user in user_db2 and passwd == user_db2[user]:
            print('login ok')
            login_db['user'] = user
            login_db['status'] = True
            res = func(*args, **kwargs)
            return res
        else:
            print('login error')
    return inner  # 加括号执行，不加括号返回内存地址

@login
def home():
    print("首页".center(40,'-'))


@login
def america(name):
    print("欧美专区".center(40,'-'))


home()
america('hqs')