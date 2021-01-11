#!/usr/bin/env python
# -*-coding:utf-8-*-
# by 'hollowman6' from Lanzhou University(兰州大学)

'''
警告：
仅供测试使用，不可用于任何非法用途！
对于使用本代码所造成的一切不良后果，本人将不负任何责任！

Warning:
For TESTING ONLY, not for any ILLEGAL USE!
I will not be responsible for any adverse consequences caused by using this code.

'''

import time
import os
import requests
import json
import random
from selenium import webdriver

session = requests.session()


def getSubmit(auToken, dailyCookie, info, now, FilledInfo):
    subApi = 'http://appservice.lzu.edu.cn/dailyReportAll/api/grtbMrsb/submit'
    subHeaders = {
        'Authorization': str(auToken),
        'Cookie': 'iPlanetDirectoryPro='+str(dailyCookie)
    }
    FilledInfo = FilledInfo['data'][0]
    info_data = info['data']['list'][0]
    sfzx = info_data['sfzx'] if info_data['sfzx'] else FilledInfo['sfzx'],
    info_data = {
        "bh": info_data['bh'],
        "xykh": info_data['xykh'],  # 校园卡号
        "twfw": "0",
        "sfzx": sfzx[0],  # 是否在校
        "sfgl": "0",
        "szsf": info_data['szsf'] if info_data['szsf'] else FilledInfo['jgsf'],
        "szds": info_data['szds'] if info_data['szds'] else FilledInfo['jgds'],
        "szxq": info_data['szxq'] if info_data['szxq'] else FilledInfo['jgxq'],
        # 是否出国
        "sfcg": info_data['sfcg'] if info_data['sfcg'] else FilledInfo['sfcg'],
        "cgdd": "",
        "gldd": "",
        "jzyy": "",
        "bllb": "0",
        "sfjctr": "0",
        "jcrysm": "",
        "xgjcjlsj": "",
        "xgjcjldd": "",
        "xgjcjlsm": "",
        # 早体温
        "zcwd": round(random.uniform(36.3, 36.8), 1) if 7 <= now < 9 and sfzx[0] == "1" else (info_data['zcwd'] if info_data['zcwd'] else 0.0),
        # 中体温
        "zwwd": round(random.uniform(36.3, 36.8), 1) if 11 <= now < 13 and sfzx[0] == "1" else (info_data['zwwd'] if info_data['zcwd'] else 0.0),
        # 晚体温
        "wswd": round(random.uniform(36.3, 36.8), 1) if 19 <= now < 21 and sfzx[0] == "1" else (info_data['wswd'] if info_data['zcwd'] else 0.0),
        "sbr": info_data['sbr'],
        "sjd": info['data']['sjd']
    }

    res = session.post(subApi, info_data, headers=subHeaders).text
    return json.loads(res), info_data


def getST(dailyCookie):
    stApi = 'http://my.lzu.edu.cn/api/getST'
    stHeaders = {
        'Cookie': 'iPlanetDirectoryPro='+str(dailyCookie)
    }
    stData = {
        'service': 'http://127.0.0.1'
    }
    stRes = session.post(stApi, stData, headers=stHeaders)
    stDic = json.loads(stRes.text)

    if stDic['state'] == 1:
        return str(stDic['data'])
    else:
        raise Exception("Error Getting ST-Token!")


def getAuthToken(stToken, cardID, dailyCookie):
    auApi = 'http://appservice.lzu.edu.cn/dailyReportAll/api/auth/login?st=' + \
        str(stToken)+'&PersonID='+str(cardID)
    auHeader = {
        'Cookie': 'iPlanetDirectoryPro='+str(dailyCookie)
    }
    auRes = session.get(auApi, headers=auHeader)
    auDic = json.loads(auRes.text)

    if auDic['code'] == 1:
        return str(auDic['data']['accessToken'])
    else:
        raise Exception("Getting AU-Token Failed!")


def getSeqMD5(cardID, auToken, dailyCookie):
    seqMD5Api = 'http://appservice.lzu.edu.cn/dailyReportAll/api/encryption/getMD5'
    seqMD5Header = {
        'Authorization': str(auToken),
        'Cookie': 'iPlanetDirectoryPro='+str(dailyCookie)
    }
    seqMD5Data = {
        'cardId': str(cardID)
    }
    seqMD5Res = session.post(seqMD5Api, seqMD5Data, headers=seqMD5Header)
    seqMD5Dic = json.loads(seqMD5Res.text)

    if seqMD5Dic['code'] == 1:
        return str(seqMD5Dic['data'])
    else:
        raise Exception("Getting card-Enc-MD5 Failed!")


def getSeqInfo(cardID, cardMD5, auToken):
    seqInfoApi = 'http://appservice.lzu.edu.cn/dailyReportAll/api/grtbMrsb/getInfo'
    seqInfoHeader = {
        'Authorization': str(auToken)
    }
    seqInfoData = {
        'cardId': str(cardID),
        'md5': str(cardMD5)
    }
    seqInfoRes = session.post(seqInfoApi, seqInfoData, headers=seqInfoHeader)
    seqInfoDic = json.loads(seqInfoRes.text)

    return seqInfoDic


def getFilledInfo(cardID, cardMD5, auToken):
    FilledInfoApi = 'http://appservice.lzu.edu.cn/dailyReportAll/api/grtbJcxxtb/getInfo'
    FilledInfoHeader = {
        'Authorization': str(auToken)
    }
    FilledInfoData = {
        'cardId': str(cardID),
        'md5': str(cardMD5)
    }
    FilledInfoRes = session.post(
        FilledInfoApi, FilledInfoData, headers=FilledInfoHeader)
    FilledInfoDic = json.loads(FilledInfoRes.text)
    if FilledInfoDic['code'] == 1:
        return FilledInfoDic
    else:
        raise Exception("Error Getting Sequence-Number!")


def getDailyToken(user, password):
    login = 'http://my.lzu.edu.cn/login'
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    option.add_argument('no-sandbox')
    option.add_argument('disable-dev-shm-usage')
    option.add_experimental_option(
        "excludeSwitches", ['enable-automation', 'enable-logging'])
    browser = webdriver.Chrome('/usr/bin/chromedriver', options=option)
    browser.get(login)
    browser.find_element_by_id('username').send_keys(user)
    browser.find_element_by_id('password').send_keys(password)
    browser.find_element_by_class_name('g-recaptcha').click()
    time.sleep(2)
    iPlanetDirectoryPro = browser.get_cookie("iPlanetDirectoryPro")
    browser.close()
    if not iPlanetDirectoryPro:
        raise Exception("Wrong password or user! If you have tried many times, it may be the ReCAPTCHA that stops you from logging.")
    dayCok = iPlanetDirectoryPro['value']
    return dayCok


def submitCard():
    timeStamp = time.strftime("%Y-%m-%d %H:%M", time.localtime())
    print("***************************")
    print(timeStamp, "正在打卡中...")
    cardID = os.environ['CARDID']
    passwd = os.environ['PASSWORD']
    dayCok = getDailyToken(cardID, passwd)
    ST = getST(dayCok)
    AuToken = getAuthToken(ST, cardID, dayCok)
    MD5 = getSeqMD5(cardID, AuToken, dayCok)
    info = getSeqInfo(cardID, MD5, AuToken)
    FilledInfo = getFilledInfo(cardID, MD5, AuToken)
    if info['code'] != 1:
        raise Exception(str(timeStamp)+" 未知错误，无法打卡!")
    now = int(time.strftime("%H", time.localtime()))
    response, info_data = getSubmit(AuToken, dayCok, info, now, FilledInfo)
    if response['code'] == 1:
        print(str(timeStamp) + " 打卡成功，" + str(response) + ((
            ("，早体温：{}".format(info_data['zcwd'])) if (7 <= now < 9) else (
                ("，中体温：{}".format(info_data['zwwd'])) if (11 <= now < 13) else (
                    ("，晚体温：{}".format(info_data['wswd'])) if (
                        19 <= now < 21) else ""
                ))) if info_data['sfzx'][0] == '1' else "，疫情期间，记得好好在家呆着!"))
    else:
        raise Exception(str(timeStamp) + "打卡失败, " +
                        str(response) + "，请提交相关问题到issue中!")


if __name__ == "__main__":
    try:
        submitCard()
    except Exception:
        print("第一次尝试失败, 再次尝试中...")
        try:
            submitCard()
        except Exception:
            print("第二次尝试失败, 再次尝试中...")
            try:
                submitCard()
            except Exception:
                print("第三次尝试失败, 再次尝试中...")
                submitCard()
