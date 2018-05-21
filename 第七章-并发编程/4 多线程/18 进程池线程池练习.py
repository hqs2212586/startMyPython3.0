# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

# 多I/O的问题采用线程池
from concurrent.futures import ThreadPoolExecutor
import requests
import time

def get(url):
    print('get %s' % url)
    # requests.get()就是目标页面下载一个文件到本地来
    response = requests.get(url)  # 对象
    time.sleep(3)   # 模拟网络延迟
    # print(response.text)    # 网页内容
    return {'url':url, 'content':response.text}


def paese(res):  # 解析，正则表达式
    res = res.result()
    print('%s parse res is %s' % (res['url'], len(res['content'])))



if __name__ == '__main__':
    urls = [
        'http://www.cnblogs.com/linhaifeng',
        'http://www.python.org',
        'http://www.openstack.org'
    ]

    pool = ThreadPoolExecutor(2)

    for url in urls:
        pool.submit(get, url).add_done_callback(paese)   # 回调函数
"""
get http://www.cnblogs.com/linhaifeng
get http://www.python.org    ——————》明显的等的效果
http://www.cnblogs.com/linhaifeng parse res is 16320
get http://www.openstack.org
http://www.python.org parse res is 49014
http://www.openstack.org parse res is 63429
"""
# 由此可分析出异步调用加回调机制使用的场景