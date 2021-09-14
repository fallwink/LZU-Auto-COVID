#!/usr/bin/env python
# -*-coding:utf-8-*-
# by 'hollowman6' from Lanzhou University(兰州大学)

from pywebpush import webpush, WebPushException
import os
import sys
import requests
import json
import urllib.parse

from requests.api import head

sckey = os.environ['SERVERCHANSCKEY']
pptoken = os.environ['PPTOKEN']
pptopic = os.environ['PPTOPIC']
tgbottoken = os.environ['TGBOTTOKEN']
tgchatids = os.environ['TGCHATID']
subsInfo = os.environ['SUBSINFO']
corpid = os.environ['CORPID']
corpsecret = os.environ['CORPSECRET']
agentid = os.environ['AGENTID']
status = sys.argv[1]
access_token = ""
head = ""
record = ""
if len(sys.argv) > 2:
    record = sys.argv[2]
    head = "工作流运行记录查看地址: " + record + "\n"
errorNotify = ""


def exwechat_get_access_token():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    params = {
        'corpid': corpid,
        'corpsecret': corpsecret
    }
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    resp_json = resp.json()
    if 'access_token' in resp_json.keys():
        return resp_json['access_token']
    else:
        raise Exception('请检查CORPID和CORPSECRET是否正确！\n' + resp.text)


def exwechat_get_ShortTimeMedia(img_url):
    media_url = f'https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token={access_token}&type=file'
    f = open(img_url, "rb").read()
    r = requests.post(media_url, files={'file': f}, json=True)
    return r.json()['media_id']


def exwechat_get_LongTimeMedia(img_url):
    media_url = f'https://qyapi.weixin.qq.com/cgi-bin/media/uploadimg?access_token={access_token}&type=file'
    f = open(img_url, "rb").read()
    r = requests.post(media_url, files={'media': f}, json=True)
    return r.json()['url']


def exwechat_send(title, digest, content):
    url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + access_token
    data = {
        "touser": "@all",
        "agentid": agentid,
        "safe": 0,
        "enable_id_trans": 0,
        "enable_duplicate_check": 0,
        "duplicate_check_interval": 1800
    }
    img_url = os.path.join(os.path.dirname(__file__), 'cover.jpg')
    data["msgtype"] = 'mpnews'
    data["mpnews"] = {
        "articles": [
            {
                "title": title,
                "thumb_media_id": exwechat_get_ShortTimeMedia(img_url),
                "author": "Hollow Man",
                "content_source_url": "https://hollowman.ml/LZU-Auto-COVID-Health-Report/",
                "content": "<a href=https://github.com/HollowMan6><img src=" + exwechat_get_LongTimeMedia(img_url) + " /></a>" + content,
                "digest": digest
            }
        ]
    }
    resp = requests.post(url, data=json.dumps(data))
    resp.raise_for_status()
    return resp


if sckey:
    info = head
    try:
        with open("information.txt") as infofile:
            info += infofile.read()
            info = urllib.parse.quote_plus(
                info.replace('\n', '\n\n'))
    except Exception as e:
        print(e)
    finally:
        try:
            if info == head:
                info += urllib.parse.quote_plus(
                    "工作流或者打卡程序存在问题，请查看运行记录并提交issue!")
                status = "failure"
            message = "%E5%A4%B1%E8%B4%A5%E2%9C%96"
            if status == "success":
                message = "%E6%88%90%E5%8A%9F%E2%9C%94"
            host = "https://sctapi.ftqq.com/"
            res = requests.get(host + sckey + ".send?title=" + message +
                               "%E5%85%B0%E5%B7%9E%E5%A4%A7%E5%AD%A6%E8%87%AA%E5%8A%A8%E5%81%A5%E5%BA%B7%E6%89%93%E5%8D%A1&desp=" + info)
            result = res.json()
            if result['data']['errno'] == 0:
                print("成功通过Sever酱将结果通知给用户!")
            else:
                errorNotify += "Server酱推送错误: " + res.text + "\n"
        except Exception as e:
            print(e)
            errorNotify += "Server酱推送错误!\n"

else:
    print("未设置SERVERCHANSCKEY，尝试使用PushPlus...")

if pptoken:
    info = head
    try:
        with open("information.txt") as infofile:
            info += infofile.read()
            info = urllib.parse.quote_plus(
                info.replace(
                    "***************************\n", "<hr>").replace('\n', '<br>'))
    except Exception as e:
        print(e)
    finally:
        try:
            if info == head:
                info += "工作流或者打卡程序存在问题，请查看运行记录并提交issue!"
                status = "failure"
            message = "%E5%A4%B1%E8%B4%A5%E2%9C%96"
            if status == "success":
                message = "%E6%88%90%E5%8A%9F%E2%9C%94"
            host = "http://www.pushplus.plus/"
            res = requests.get(host + "send?token=" + pptoken + "&title=" + message +
                               "%E5%85%B0%E5%B7%9E%E5%A4%A7%E5%AD%A6%E8%87%AA%E5%8A%A8%E5%81%A5%E5%BA%B7%E6%89%93%E5%8D%A1&content=" + info
                               + "&template=html&topic=" + pptopic)
            result = res.json()
            if result['code'] == 200:
                print("成功通过PushPlus将结果通知给相关用户!")
            else:
                errorNotify += "PushPlus推送错误: " + res.text + "\n"
        except Exception as e:
            print(e)
            errorNotify += "PushPlus推送错误!\n"
else:
    print("未设置PPTOKEN，尝试推送到Telegram...")

if tgbottoken:
    if tgchatids:
        index = 1
        for tgchatid in tgchatids.replace(' ', '').split(','):
            if tgchatid:
                info = head
                try:
                    with open("information.txt") as infofile:
                        info = "\n\n" + info
                        info += infofile.read()
                except Exception as e:
                    print(e)
                finally:
                    try:
                        if info == head:
                            info += "工作流或者打卡程序存在问题，请查看运行记录并提交issue!"
                            status = "failure"
                        message = "%E5%A4%B1%E8%B4%A5%E2%9C%96"
                        if status == "success":
                            message = "%E6%88%90%E5%8A%9F%E2%9C%94"
                        info = urllib.parse.quote_plus(info.replace(
                            "***************************\n", "---------------------------------------------------\n").replace(
                            '-', '\\-').replace('.', '\\.').replace('{', '\\{').replace('}', '\\}').replace('!', '\\!').replace('=', '\\='))
                        host = "https://api.telegram.org/bot"
                        res = requests.get(host + tgbottoken + "/sendMessage?chat_id=" + tgchatid + "&text=*%20_%20__" + message +
                                           "%E5%85%B0%E5%B7%9E%E5%A4%A7%E5%AD%A6%E8%87%AA%E5%8A%A8%E5%81%A5%E5%BA%B7%E6%89%93%E5%8D%A1__%20_%20*" + info
                                           + "&parse_mode=MarkdownV2")
                        result = res.json()
                        if result['ok']:
                            print("成功通过Telegram将结果通知给用户" + str(index) + "!")
                        else:
                            errorNotify += "Telegram用户" + \
                                str(index) + "推送错误: " + res.text + "\n"
                    except Exception as e:
                        print(e)
                        errorNotify += "Telegram用户" + str(index) + "推送错误!\n"
            index += 1
    else:
        print("未设置TGCHATID，无法推送到Telegram!")
else:
    print("未设置TGBOOTTOKEN！")

if subsInfo:
    data = {
        "requireInteraction": True,
        "vibrate": [200, 100, 200],
        "icon": "https://hollowman.ml/LZU-Auto-COVID-Health-Report/lzu.png",
        "body": "点击通知查看打卡记录工作流!",
        "title": "失败✖ 兰州大学自动健康打卡"
    }
    if status == "success":
        data['title'] = "成功✔ 兰州大学自动健康打卡"
    if record:
        data['data'] = record
    else:
        data['data'] = "https://github.com/HollowMan6/LZU-Auto-COVID-Health-Report"
    try:
        webpush(
            subscription_info=json.loads(subsInfo),
            data=json.dumps(data),
            vapid_private_key="tUCZ-8DGMlUhr3ntyN4PQoDbALJSBnv8yZXhi4XX1iI",
            vapid_claims={
                "sub": "mailto:hollowman@hollowman.ml",
            }
        )
        print("成功通过浏览器订阅消息推送将结果通知给相关用户!")
    except WebPushException as ex:
        print("I'm sorry, but: {}", repr(ex))
        # Mozilla returns additional information in the body of the response.
        if ex.response and ex.response.json():
            extra = ex.response.json()
            print("Remote service replied with a {}:{}, {}",
                  extra.code,
                  extra.errno,
                  extra.message
                  )
        errorNotify += "浏览器订阅消息推送错误!\n"
else:
    print("未设置SUBSINFO！")

if corpid:
    info = head
    if corpsecret:
        if agentid:
            access_token = exwechat_get_access_token()
            try:
                with open("information.txt") as infofile:
                    info += "<font size=2>"
                    info += infofile.read()
                    info = info.replace("***************************\n",
                                                    "<hr/>").replace("\n", "<br/>")
                    info += "</font>"
            except Exception as e:
                print(e)
            finally:
                try:
                    if info == head:
                        info += "<hr/>工作流或者打卡程序存在问题，请查看运行记录并提交issue!"
                        status = "failure"
                    message = "打卡失败✖"
                    if status == "success":
                        message = "打卡成功✔"
                    info += "<hr/><h3>点击下方<b><font color=#1A5FB4>阅读原文</font></b>来管理自动打卡仓库</h3>"
                    res = exwechat_send(message, "兰州大学自动健康打卡", info)
                    result = res.json()
                    if result['errcode'] == 0:
                        print("成功通过企业微信将结果通知给用户!")
                    else:
                        errorNotify += "企业微信推送错误: " + res.text + "\n"
                except Exception as e:
                    print(e)
                    errorNotify += "企业微信推送错误!\n"
        else:
            print("未设置AGENTID，无法推送到企业微信！")
    else:
        print("未设置CORPSECRET，无法推送到企业微信！")
else:
    print("未设置CORPID！")

if errorNotify:
    raise Exception(errorNotify)
