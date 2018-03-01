
menus = [
    {
        'text': '北京',
        'children': [
            {'text': '朝阳', 'children': []},
            {'text': '昌平', 'children': [
                {'text': '沙河', 'children': []},
                {'text': '回龙观', 'children': []}
            ]},
        ]
    },
    {
        'text': '上海',
        'children': [
            {'text': '宝山', 'children': []},
            {'text': '金山', 'children': []},
        ]
    }
]
'''
    递归练习题：（深度查询）
        1、打印所有的节点
        2、输入一个节点名字，沙河，要遍历找，找到即打印它，并返回true
'''

def node_print(name):     # 打印节点
    for node in name:
        print(node['text'])
        node_print(node['children'])


def node_search(menus,name):    # 查找节点
    for node in menus:
        if name != node['text']:
            node_search(node['children'], name)
        else:
            print(node)

print(node_print(menus))

name = input("节点名称：")
node_search(menus,name)