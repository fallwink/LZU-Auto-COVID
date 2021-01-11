#!/usr/bin/env python
# -*-coding:utf-8-*-
# by 'hollowman6' from Lanzhou University(兰州大学)

import os
import requests
import json
import urllib.parse

sckey = os.environ['SERVERCHANSCKEY']
info = ""
if sckey:
    try:
        with open("information.txt") as infofile:
            info = urllib.parse.urlencode(infofile.read())
    except Exception as e:
        print(e)
    finally:
        if not info:
            info = "工作流或者打卡程序存在问题，请查看运行记录并提交issue!"
        res = requests.get("http://sc.ftqq.com/" + sckey +
                        ".send?text=%E5%85%B0%E5%B7%9E%E5%A4%A7%E5%AD%A6%E8%87%AA%E5%8A%A8%E5%81%A5%E5%BA%B7%E6%89%93%E5%8D%A1%E8%BF%90%E8%A1%8C%E7%BB%93%E6%9E%9C&desp=" + info)
        result = json.loads(res.text)
        if result['errno']==0:
            print("成功将结果通知给用户!")
        else:
            raise Exception(res.text)
else:
    print("未设置SERVERCHANSCKEY，程序退出...")
