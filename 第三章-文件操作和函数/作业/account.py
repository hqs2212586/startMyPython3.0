"""
1.输入用户名密码，正确后登陆系统，打印如下信息：
    1.修改个人信息
    2.打印个人信息
    3.修改密码
2.每个选项写一个方法
3.登录时输错3次退出程序
"""


def print_info(account_dic,username):
    person_data = account_dic[username]
    info = '''
    ----------------------
    Name:   %s
    Age:    %s
    Job:    %s
    Dept:   %s
    ----------------------
    '''%(person_data[0],
         person_data[2],
         person_data[3],
         person_data[4],
         )
    print(info)


def change_info(account_dic,username):
    """
    change user info ,思路如下
    1. 把这个人的每个信息打印出来， 让其选择改哪个字段，用户选择了的数字，正好是字段的索引，这样直接 把字段找出来改掉就可以了
    2. 改完后，还要把这个新数据重新写回到account.txt，由于改完后的新数据 是dict类型，还需把dict转成字符串后，再写回硬盘
    :param account_dic: all account's data
    :param username: username
    :return: None
    """
    person_data = account_dic[username]
    print("person data: ",person_data)
    column_names = ['Username','Password',]
    for index,k in enumerate(person_data):
        if index > 1:...


def save_file():...


account_file = 'account.txt'
f = open(account_file,"r+")
raw = f.readlines()  # 数组数据结构
accounts = {}
# 将账户数据读出来，变为dict结构，方便查询
for i in  raw:
    i = i.strip()
    if not i.startswith("#"):  # 排除注释
        items = i.split(",")  # 逗号分隔  ['hqs', '123456', '29', 'engineer', 'IT']
        accounts[items[0]] = items
# print(accounts)  # {'hqs': ['hqs', '123456', '29', 'engineer', 'IT'], 'rain': ['rain', 'dadada', '27', 'teacher', 'edu'], 'admin': ['admin', 'admin', '22', 'administrator', 'admin']}

menu = '''
1.打印个人信息
2.修改个人信息
3.修改密码
'''
count = 0
while count <3:
    username = input("请输入用户名：").strip()
    password = input("请输入用户密码：").strip()
    if username in accounts:
        if password == accounts[username][1]:
            print("welcome %s".center(50,'-') % username)
            while True: # 使用户可以一直停留在这一层
                print(menu)  # 打印菜单
                user_choice = input(">>>[按q退出]").strip()
                if user_choice.isdigit():
                    user_choice = int(user_choice)
                    if user_choice == 1:
                        print_info(accounts,username)
                    elif user_choice == 2:
                        change_info()

                elif user_choice == 'q':
                    exit("bye.")
        else:
            print("错误的用户名或密码！")
    else:
        print("用户名不存在！")

    count += 1
else:
    print("Too many attempt!")