
# 数据结构：

menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{}
}

# 需求：
# 可依次选择进入各子菜单
# 可从任意一层往回退到上一层
# 可从任意一层退出程序
# 所需新知识点：列表、字典

'''
tag = True
while tag:
    # 一级菜单
    for k in menu:
        print(k)
    # strip()去除字符串首尾空格赋值给choice,省、市
    choice = input(">:").strip()
    if choice in menu:

        while tag:
            # 二级菜单
            for k in menu[choice]:
                print(k)
            # 输入并确认，区
            choice2 = input(">>:").strip()
            if choice2 in menu[choice]:

                while tag:
                    # 三级菜单
                    for k in menu[choice][choice2]:
                        print(k)
                    # 打印并确认地区
                    choice3 = input(">>>").strip()
                    if choice3 in menu[choice][choice2]:
                        # 打印下属公司
                        # for k in menu[choice][choice2][choice3]:
                            # print(k)
                            # continue
                    elif choice3 == "back":
                        # 返回上一级
                        break
                    elif choice3 == "exit":
                        tag = False
                        print("good bye!")
                    else:
                        print("节点不存在")
                        # 重新执行循环
                        continue
            elif choice2 == "back":
                # 返回上一级
                break
            elif choice2 == "exit":
                tag = False
                print("good bye!")
            else:
                print("节点不存在")
                continue
    elif choice == "back":
        # 返回上一级
        print("已经是最顶层目录")
    elif choice == "exit":
        tag = False
        print("good bye!")
    else:
        print("节点不存在")
        continue
'''

current_layer = menu # 当前层
layers = []
tag = True

while tag:
    # 一级菜单
    for k in current_layer:
        print(k)
    choice = input(">:").strip()
    # 二级菜单
    if choice in current_layer:
        # 进入下一级菜单，保存当前菜单
        layers.append(current_layer)
        # 二级菜单赋给当前层
        current_layer = current_layer[choice]

    elif choice == "back":
        if len(layers) != 0:
            # pop删除列表最后一个元素，并返回删除后最后一个元素
            current_layer = layers.pop()
        else:
            print("已经是最顶层目录！")
    elif choice == "exit":
        tag = False
        print("good bye!")
    else:
        continue