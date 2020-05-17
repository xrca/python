#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/20 0020 21:11
# @File  : amap.py

import time
import requests
import json
import random

from queue import Queue

dffdfdf = 0

class AmapSearch:

    def __init__(self):

        # 请求查询结果链接
        self.get_page_url = 'https://www.amap.com/service/poiInfo'
        self.data_queue = Queue()

        self.start()

    def get_page(self, params):

        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            # 'amapuuid': 'd0107596-5479-4ed0-84a4-52b77365b15c',
            'Host': 'www.amap.com',
            # 必须项，可保持不变
            'Referer': 'https://www.amap.com/search?query=%E9%A4%90%E9%A5%AE&city=440100&geoobj=113.334885%7C23.128997%7C113.345201%7C23.143948&zoom=16',
            # 'Sec-Fetch-Mode': 'cors',
            # 'Sec-Fetch-Site': 'same-origin',

            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'Cookie': 'acw_tc=2760825a15873748050738988ecd6fea20edfecff3d171831d91f9af84859f; UM_distinctid=17196e95cfb25f-00c0c432278563-33365801-1fa400-17196e95cfc93c; cna=FP4jFy52XywCAXhVfIyhSQML; _uab_collina=158737480969931755948885; guid=b824-ae1b-4543-0d35; CNZZDATA1255626299=1496368942-1587370159-https%253A%252F%252Fwww.baidu.com%252F%7C1587370159; l=eBLGXSoHQ4wY8IO8BO5MRmki0g_9BBRfhsPrgXzYtIHca6T5dKozPNQcd2_Xfdtjgt5bsUtPjiOhPRnB-j4T5xNllYtH3YLEVa9w8e1..; isg=BJWV0Ud1Z0kjykO17TJORFKvpJFPkkmkxUyBWhc8oIxCbrNg1-MLdkZoOHJY7mFc'
        }

        # 尝试5次
        for i in range(5):
            try:
                res = requests.get(self.get_page_url, params=params, headers=headers)
                if res.status_code == 200:
                    return res.text

            except Exception as err:
                print(err)
                
            time.sleep(random.randint(2, 5))

        return None

    def get_lat_lng_keyword(self, lat_lng_list, keyword):
        """ 根据区域的对角经纬度和关键词获取商家信息
        """
        pagesize = 30
        pagenum = 1
        geoobj = '|'.join([str(data) for data in lat_lng_list])

        while True:

            # 请求参数
            params = {
                'query_type': 'TQUERY',
                'pagesize': str(pagesize),
                'pagenum': str(pagenum),
                'qii': 'true',
                'cluster_state': '5',
                'need_utd': 'true',
                'utd_sceneid': '1000',
                'div': 'PC1000',
                'addr_poi_merge': 'true',
                'is_classify': 'true',
                'zoom': '16',
                'city': '3201',
                'geoobj': geoobj,
                'keywords': keyword,
            }

            res_text = self.get_page(params)
            #print(res_text)
            if res_text is not None:
                res_json = json.loads(res_text)
                # print(res_json)
                if res_json is not None:

                    data_list = []
                    poi_list = res_json['data']['poi_list']
                    for poi in poi_list:
                        data_list.append(poi['name'])
                        data_list.append(poi['cityname'])
                        data_list.append(poi['address'])
                        # 后续分离出座机和手机
                        data_list.append(poi['tel'])
                        data_list.append(poi['latitude'])
                        data_list.append(poi['longitude'])
                        print("==============================================================")
                        print("名称：" + poi['name'] + "，经纬度：" + poi['latitude'] + "," + poi['longitude'] + "，地址：" + poi['address'])
                        #self.data_queue.put(data_list)

                    # 总数据，判断是否结束
                    total = int(res_json['data']['total'])
                    if pagesize * pagenum >= total:
                        break
                    else:
                        pagenum += 1
                        time.sleep(random.randint(2, 3))
            else:
                time.sleep(random.randint(2, 3))

    def start(self):

        #lat_lng_list = '113.334885|23.128997|113.345201|23.143948'.split('|')
        #lat_lng_list = '118.125|31.11328125|119.53125|32.6953125'.split('|')
        lat_lng_list = '118.125|32.6953125|119.53125|31.11328125'.split('|')
        keywords = '肯德基'
        self.get_lat_lng_keyword(lat_lng_list, keywords)


def main():
    amap = AmapSearch()


if __name__ == '__main__':
    main()