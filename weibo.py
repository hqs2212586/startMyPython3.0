import requests  # 网络请求 pip install requests


for n in range(10):
    #网址 url
    url = 'https://m.weibo.cn/api/comments/show?id=4192582252610831&page=4'

    # 请求网址
    html = requests.get(url)

    # 打印网页信息
    # print(html.status_code) ＃可以使用lamda代替for循环实现
    for m in range(len(html.json()['data']['data'])):
        try:
            # ID信息
            data_id = html.json()['data']['data'][m]['user']['id']
            # 写入文件
            with open('/Users/huangqiushi/Desktop/weibo.txt','r') as f:
                f.write(data_id + '\n' * 2)
            print(html.json()['data']['data'][m]['user']['id'])
        except:
            print('error')