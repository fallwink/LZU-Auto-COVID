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
        "bh": info_data['bh'],  # 编号
        "xykh": info_data['xykh'],  # 校园卡号
        "twfw": "0",  # 体温范围(0为小于37.3摄氏度)
        "sfzx": sfzx[0],  # 是否在校(0离校，1在校)
        "sfgl": "0",  # 是否隔离(0正常，1隔离)
        "szsf": info_data['szsf'] if info_data['szsf'] else FilledInfo['xszsf'],  # 所在省份（没有打卡记录则是基本信息中现所在省份）
        "szds": info_data['szds'] if info_data['szds'] else FilledInfo['xszds'],  # 所在地级市（没有打卡记录则是基本信息中现所在地级市）
        "szxq": info_data['szxq'] if info_data['szxq'] else FilledInfo['xszxq'],  # 所在县/区（没有打卡记录则是基本信息中现所在县/区）
        "sfcg": info_data['sfcg'] if info_data['sfcg'] else FilledInfo['sfcg'],  # 是否出国（没有打卡记录则是基本信息中是否出国）
        "cgdd": info_data['cgdd'] if info_data['cgdd'] else FilledInfo['cgdd'],  # 出国地点（没有打卡记录则是基本信息中出国地点）
        "gldd": "",  # 隔离地点
        "jzyy": "",  # 就诊医院
        "bllb": "0",  # 是否被列入(疑似/确诊)病例(0没有，其它为疑似/确诊)
        "sfjctr": "0",  # 是否接触他人(0否，1是)
        "jcrysm": "",  # 接触人员说明
        "xgjcjlsj": "", # 相关接触经历时间
        "xgjcjldd": "", # 相关接触经历地点
        "xgjcjlsm": "", # 相关接触经历说明
        "zcwd": round(random.uniform(36.3, 36.8), 1) if 7 <= now < 9 and sfzx[0] == "1" else (info_data['zcwd'] if info_data['zcwd'] else 0.0),
        # 早晨温度(体温)
        "zwwd": round(random.uniform(36.3, 36.8), 1) if 11 <= now < 13 and sfzx[0] == "1" else (info_data['zwwd'] if info_data['zcwd'] else 0.0),
        # 中午温度(体温)
        "wswd": round(random.uniform(36.3, 36.8), 1) if 19 <= now < 21 and sfzx[0] == "1" else (info_data['wswd'] if info_data['zcwd'] else 0.0),
        # 晚上温度(体温)
        "sbr": info_data['sbr'], # 上报人
        "sjd": info['data']['sjd'] # 时间段
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
        print("Error Getting ST-Token!")
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
        print("Getting AU-Token Failed!")
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
        print("Getting card-Enc-MD5 Failed!")
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
        print("Error Getting Sequence-Number!")
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
    if not (user.isdigit() and len(user) == 12):
        user = browser.execute_script("a = document.getElementById('personUserECard'); if(a) return a.innerText")
    browser.close()
    if not iPlanetDirectoryPro:
        print("Wrong password or user! Please make sure you set related Action Secrets correctly.")
        raise Exception("Wrong password or user! Please make sure you set related Action Secrets correctly.")
    dayCok = iPlanetDirectoryPro['value']
    return dayCok, user


def submitCard():
    timeStamp = time.strftime("%Y-%m-%d %H:%M", time.localtime())
    print("***************************")
    print(timeStamp, "正在打卡中...")
    cardID = os.environ['CARDID']
    passwd = os.environ['PASSWORD']
    dayCok, cardID = getDailyToken(cardID, passwd)
    ST = getST(dayCok)
    AuToken = getAuthToken(ST, cardID, dayCok)
    MD5 = getSeqMD5(cardID, AuToken, dayCok)
    info = getSeqInfo(cardID, MD5, AuToken)
    FilledInfo = getFilledInfo(cardID, MD5, AuToken)
    if info['code'] != 1:
        print(str(timeStamp)+" 未知错误，无法打卡!")
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
        print(str(timeStamp) + "打卡失败, " +
                        str(response) + "，请提交相关问题到issue中!")
        raise Exception(str(timeStamp) + "打卡失败, " +
                        str(response) + "，请提交相关问题到issue中!")


if __name__ == "__main__":
    if not os.environ['CARDID']:
        raise Exception("未设置Actions Secrets变量CARDID，请检查！")
    if not os.environ['PASSWORD']:
        raise Exception("未设置Actions Secrets变量PASSWORD，请检查！")
    try:
        submitCard()
    except Exception:
        print(time.strftime("%Y-%m-%d %H:%M", time.localtime()), "第一次尝试失败, 再次尝试中...")
        try:
            submitCard()
        except Exception:
            print(time.strftime("%Y-%m-%d %H:%M", time.localtime()), "第二次尝试失败, 再次尝试中...")
            try:
                submitCard()
            except Exception:
                print(time.strftime("%Y-%m-%d %H:%M", time.localtime()), "第三次尝试失败, 再次尝试中...")
                submitCard()
