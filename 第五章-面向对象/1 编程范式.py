"""
面向过程编程：核心是过程二字，过程指的是解决问题的步骤，设计一条流水线。  机械式思维方式
优点：复杂问题流程化，进而简单化。
缺点：可扩展性差、可维护性差
适用于改动比较小的应用场景，去做一些一次性任务，比如自动部署脚本
"""
import json
def interactive():
    name = input('>>: ').strip()
    pwd = input('>>: ').strip()
    email = input('>>: ').strip()
    return {
        'name': name,
        'pwd': pwd,
        'email': email
    }


def check(user_info):
    is_valid = True

    if len(user_info['name']) == 0:
        print('用户名不能为空')
        is_valid = False
    if len(user_info['pwd']) < 0:
        print('密码不能少于6位')
        is_valid = False

    return {
        'is_valid': is_valid,
        'user_info': user_info
    }


def register(check_info):
    if check_info['is_valid']:
        with open('db.json', 'w', encoding='utf-8') as f:
            json.dump(check_info['user_info'], f)


def main():
    user_info = interactive()

    check_info = check(user_info)

    register(check_info)


if __name__ == '__main__':
    main()


"""
面向对象编程：核心就是对象二字，对象就是特征与技能的结合体
优点：可扩展性强、
缺点：编程复杂度高
应用场景：用户需求经常变化，互联网应用，游戏，企业内部应用
"""