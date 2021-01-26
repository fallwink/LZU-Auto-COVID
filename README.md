# 兰州大学疫情期间自动定时健康打卡工作流

[![last-commit](https://img.shields.io/github/last-commit/HollowMan6/LZU-Auto-COVID-Health-Report)](../../graphs/commit-activity)
![Python package](../../workflows/Python%20package/badge.svg)
![GitHub Actions LZU Auto COVID Health Report](../../workflows/GitHub%20Actions%20LZU%20Auto%20COVID%20Health%20Report/badge.svg)

[![Followers](https://img.shields.io/github/followers/HollowMan6?style=social)](https://github.com/HollowMan6?tab=followers)
[![watchers](https://img.shields.io/github/watchers/HollowMan6/LZU-Auto-COVID-Health-Report?style=social)](../../watchers)
[![stars](https://img.shields.io/github/stars/HollowMan6/LZU-Auto-COVID-Health-Report?style=social)](../../stargazers)
[![forks](https://img.shields.io/github/forks/HollowMan6/LZU-Auto-COVID-Health-Report?style=social)](../../network/members)

[![Open Source Love](https://img.shields.io/badge/-%E2%9D%A4%20Open%20Source-Green?style=flat-square&logo=Github&logoColor=white&link=https://hollowman6.github.io/fund.html)](https://hollowman6.github.io/fund.html)
[![GPL Licence](https://img.shields.io/badge/license-GPL-blue)](https://opensource.org/licenses/GPL-3.0/)
[![Repo-Size](https://img.shields.io/github/repo-size/HollowMan6/LZU-Auto-COVID-Health-Report.svg)](../../archive/master.zip)

[![Total alerts](https://img.shields.io/lgtm/alerts/g/HollowMan6/LZU-Auto-COVID-Health-Report.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/HollowMan6/LZU-Auto-COVID-Health-Report/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/HollowMan6/LZU-Auto-COVID-Health-Report.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/HollowMan6/LZU-Auto-COVID-Health-Report/context:python)
[![](https://images.microbadger.com/badges/image/hollowman6/lzu-auto-covid-health-report.svg)](https://microbadger.com/images/hollowman6/lzu-auto-covid-health-report)

(English version is down below)

### 好用记得收藏(右上角**加星★Star**)哦!

[Python库依赖](../../network/dependencies)

[自动打卡脚本](LZU-Auto-COVID-Health-Report.py)

[工作流](.github/workflows/autoreport.yml)

## 使用方法

因为大陆网络环境导致图片无法显示的可以前往Gitee查看(下述操作步骤仍然要在Github平台上完成哦!)：https://gitee.com/hollowman6/LZU-Auto-COVID-Health-Report#%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95

（强烈建议你首先自己打一次卡之后再使用本软件，从而初始化平台打卡系统中的数据。本软件将会一直沿用你在系统中最新填报的`是否在校`、`所在省市区`，`是否出国`、`出国地点`打卡信息，并会一直上报最健康的状态。）

对于直接在Github Actions上使用工作流进行自动打卡，你可以首先fork本仓库，之后在你fork的仓库中进行相关设置。

1. 首先，按下图所示点击1，2，3的次序，进入新建Actions secrets的界面。我们需要两个Actions secrets，一个的Name为`CARDID`，value为你的兰州大学校园卡号(也可接受兰大邮箱账号(不含@lzu.edu.cn后缀))；另一个的Name为`PASSWORD`，value为你的兰州大学个人工作台的账户密码（和你的兰大邮箱密码相同）。依次按上述要求创建这两个secrets即可。创建完成后你将在右下部分看到两个Actions secrets。
![](img/secrets.png)

2. 然后，按下图所示点击1，2，3，4的次序，你可以手动触发工作流的执行来进行测试。（**注意：** 如果因为你多次重复因为账号密码错误登录失败，很有可能会导致验证码的出现，此时程序会被阻止自动登录。因而请确保你已经在[兰州大学个人工作台](http://my.lzu.edu.cn:8080/login?service=http://my.lzu.edu.cn)处测试过你的账号密码是正确的。）另外工作流还自动会在北京时间每天的~~7点，11点，19点~~7点寒暑假时间(1月，2月，7月，8月)自动运行。（因为Github方的原因，可能会有半小时左右的延迟）
![](img/workflow.png)

3. 点开任意一个运行记录，依次点开下图所示1，2，你可以看到运行记录以及错误说明。
![](img/run.png)

4. 如果某次因为某些因素工作流运行失败，GitHub会自动发邮件提醒工作流运行失败，从而方便自己手动打卡。

5. 将来某一天疫情过去了，不需要再打卡，你可以按下图操作关闭：
![](img/cancel.png)

6. **新**：增加可选的遇到打卡失败的情况，自动重启工作流，并等待一段时间后再次自动打卡。如果你需要这个功能，则请创建一个Personal Access Token, [获取教程](https://docs.github.com/cn/github/authenticating-to-github/creating-a-personal-access-token#creating-a-token)(第7步令牌的作用域权限你只需要选中workflow这一栏即可)。然后创建一个Name为`GPATOKEN`，value为你的令牌值的Actions Secret。

默认再次打卡等待时间为30分钟，如果你有需要可以将[这里](
https://github.com/HollowMan6/LZU-Auto-COVID-Health-Report/blob/main/.github/workflows/autoreport.yml#L59)的`30m`替换为你想要的数值，这里的时间遵循Linux sleep 函数对应时间语法：一个数字后接 `s` 对应秒, `m` 对应分钟等。

如果是因为本仓库程序本身因为失效而导致的报错，你可以取消正在运行中的工作流从而终止这一循环。

## 可选：微信推送打卡结果

### PushPlus(推荐)

首先[登录PushPlus](https://pushplus.hxtrip.com/login)，然后在pushplus网站中找到您的token，仿照[使用方法](#使用方法)步骤1，创建一个Name为`PPTOKEN`，value为您的token值的TokenActions secret，就可以进行一对一推送自动打卡结果相关信息。

如果需要对多个账号推送自动打卡结果相关信息，即一对多推送，还需要另外新建一个群组，记下群组编码，然后创建一个Name为`PPTOPIC`，value为您的群组编码的Actions secret。

![](https://pushplus.hxtrip.com/doc/img/c1.png)

### Server酱

如使用[Server酱](http://sc.ftqq.com/)来实现，它的配置方法请参考其说明文档。

然后，你只需要仿照[使用方法](#使用方法)步骤1，创建一个Name为`SERVERCHANSCKEY`，value为[你的SCKEY调用代码值](http://sc.ftqq.com/?c=code)的Actions secret即可自动让仓库的工作流通过Server酱为你推送自动打卡结果相关信息。

*效果示意*：

推送效果：
![](img/ServerChan.jpg)

点开详情：
![](img/ServerChanMessage.jpg)

### Server酱测试号版

如果要使用[Server酱测试号版](https://sct.ftqq.com/)，请创建一个/修改Name为`SERVERCHANSCKEY`，value为[你的SendKey值](https://sct.ftqq.com/sendkey)的Actions secret。另外创建一个Name为`OPENID`的Actions secret，如果value值为`0`则是通过公众号仅发给自己。否则将value值设定为关注你测试公众号的那个用户的微信号openid，这时将发给自己的同时还会发送给那个指定用户。

如果需要转换回普通的Sever酱请将`OPENID` Actions secret删除即可。

## 自行配置工作流

你可以自行创建一个仓库并自行配置工作流进行使用，[示例工作流文件](.github/workflows/autoreport-docker.yml)

### 输入

#### 必须

* CARDID: 兰大校园卡号
* PASSWORD: 兰大邮箱卡号

#### 可选

* DELAYS: 设置打卡时间延迟
* SERVERCHANSCKEY: Server酱 SCKEY
* OPENID: Server酱测试号版 微信公众号用户OpenID
* PPTOKEN: PushPlus Token
* PPTOPIC: PushPlus 群组编码

### 示例

```yaml
- name: Auto COVID Health Report
  uses: HollowMan6/LZU-Auto-COVID-Health-Report@master
  with:
    CARDID: ${{ secrets.CARDID }}
    PASSWORD: ${{ secrets.PASSWORD }}
    DELAYS: ${{ github.event.inputs.delays }}
    SERVERCHANSCKEY: ${{ secrets.SERVERCHANSCKEY }}
    OPENID: ${{ secrets.OPENID }}
    PPTOKEN: ${{ secrets.PPTOKEN }}
    PPTOPIC: ${{ secrets.PPTOPIC }}
```

## Docker

Docker Hub: https://hub.docker.com/r/hollowman6/lzu-auto-covid-health-report

如果你需要通过Docker运行，只需要将上述Actions Secret变量名和值分别设置为环境变量(另外增加一个DELAYS为打卡等待时间，值同[使用方法](#使用方法)步骤6中要求)，然后执行下述命令即可：
```bash
docker run -it \
    -e CARDID=$CARDID \
    -e PASSWORD=$PASSWORD \
    -e DELAYS=$DELAYS \
    -e SERVERCHANSCKEY=$SERVERCHANSCKEY \
    -e OPENID=$OPENID \
    -e PPTOKEN=$PPTOKEN \
    -e PPTOPIC=$PPTOPIC \
    -e DELAYS=$DELAYS \
    hollowman6/lzu-auto-covid-health-report
```

**创建**

```bash
docker build -t hollowman6/lzu-auto-covid-health-report .
```

该Docker镜像也可以在云服务器中结合Kubernetes的CronJob运行等，可能性无限多。

## Q&A

*注:* 如要在自己的Linux服务器上使用crontab执行定时任务来进行自动打卡，推荐使用[Docker](#docker)。你也可以clone本仓库，安装好相关Python依赖后改编[entrypoint.sh](entrypoint.sh)文件中python程序的路径，将上述Actions Secret变量名和值分别设置为系统环境变量(另外增加一个DELAYS为打卡等待时间，值同[使用方法](#使用方法)步骤6中要求)，即可运行。

1. 怎么查看自己有没有打卡成功？

如果你指的是兰大app里面的健康打卡系统，请把兰大app里面的健康打卡系统中“教职工是否在兰（学生是否在校）”那一栏选中状态取消并手动打一次卡。成功打卡后，打开APP会提示“当日填报完成，如变化请更新！”。

如果你指的是Github Actions里面请直接查看运行记录。workflow运行无报错，则打卡成功。失败Github会站内消息提示workflow运行失败。

当然另外你还可以配置使用[sever酱微信推送](#可选微信推送打卡结果)。

2. 打卡应用里面没有你给的那个体温选项

返校的时候，如果学校要一日三报，是会有的。

在假期不需要一日三次上报体温，这个功能是为未来返校的时候做的。我的程序会自动判断当前是否在校，如果不在校是不会有体温数据的（都是0.0），另外每次post数据都是要有这一项的。

另外设置的Github Actions是每日三次运行程序，如果你不需要，可以将[这里](
https://github.com/HollowMan6/LZU-Auto-COVID-Health-Report/blob/main/.github/workflows/autoreport.yml#L10)
更改为`    - cron: '0 23 * * *' # Schedule on CST 7 everyday`，
即每日只在北京时间早上7点运行。

**警告**：

***仅供测试使用，不可用于任何非法用途！***

***对于使用本代码所造成的一切不良后果，本人将不负任何责任！***
# LZU Auto COVID Health Report using Github Action

### Please **★Star** if you think it's great!

[Python library dependency](../../network/dependencies)

[Auto Report Script](LZU-Auto-COVID-Health-Report.py)

[Workflow](.github/workflows/autoreport.yml)

## Usage

(It is strongly recommended that you first report your own situation by yourself before using this software so that the system's data can be initialized. This software will always use the `at university`, `your location`, `whether at abroad`, `abroad location` you kept in the system, and report the healthiest status.)

To auto report with Github Actions workflow, you can fork this repository first, and then set related settings in your forked repository.

1. First, click in the order of 1, 2 and 3 as shown in the figure below to enter creating the new actions secrets interface. We need two actions secrets, one name is `CARDID`, value is your student card number of Lanzhou University(or the LZU email account user name(without `@lzu.edu.cn`)); the other is `PASSWORD`, value is the account password of your personal workbench of Lanzhou University(It's the same as your email password). Create these two secrets in turn according to the above requirements. After the creation, you will see two actions secrets as in the lower right section.
![](img/secrets.png)

1. Then, click in the order of 1, 2, 3 and 4 as shown in the figure below. You can manually trigger the execution of workflow to test. (**Note:** if you repeatedly fail to log in because of the wrong account or password, the program may be likely to be prevented from logging in automatically by reCAPTCHA. So please make sure that you can successfully logged into [Lanzhou University personal workbench](http://my.lzu.edu.cn:8080/login?service=http://my.lzu.edu.cn) with your account number and password and that they are correct.) In addition, the workflow will automatically run at ~~7:00, 11:00 and 19:00~~7:00 Summer/Winter Holiday Time (January, February, July, August) Beijing time every day. (Due to the mechanism realized by Github, there may exist a delay for about half an hour.)
![](img/workflow.png)

3. Click any running record, and then click in the order of 1 and 2 as shown in the figure below. You can see the running record and error description.
![](img/run.png)

4. If the workflow fails due to some errors, GitHub will automatically send an email to remind the workflow of failure, so on receiving this, you can report by yourself.

5. One day, when the COVID-19 is over, and you don't need to report your health any more. You can disable it according to the following figure:
![](img/cancel.png)

6. **NEW**: Add the optional option to restart the workflow automatically in case of Auto Report in failure, and wait for a period of time to re-run workflow again automatically. If you need this, please create a Personal Access Token, [Here's Guides to create](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token#creating-a-token)(In step 7 scopes or permissions, you only need to select the `workflow` row). Then create an Actions Secret with the name of `GPATOKEN` and the value with your token.

The default waiting time is 30 minutes. You can replace `30m` [here](
https://github.com/HollowMan6/LZU-Auto-COVID-Health-Report/blob/main/.github/workflows/autoreport.yml#L59) with the time you want. The time here  follows the Linux sleep syntax for time units: a number followed by `s` for seconds, `m` for minutes, etc.

If the error is caused by the repository program itself, you can cancel the running workflow to terminate the loop.

## Optional: WeChat push results

### PushPlus(Recommended)

First [log into pushplus](https://pushplus.hxtrip.com/login), and then find your token in pushplus website, follow [Usage](#Usage) step 1, create a actions secret with the name of `PPTOKEN` and the value of your token value, and then one-to-one push the related information of automatic reporting results.

If you need to push the related information of automatic reporting results to multiple Wechat accounts, that is, one-to-many push, you need to create a group, write down the group code, and then create an actions secret with the name of `PPTOPIC` and the value of your group code.

![](https://pushplus.hxtrip.com/doc/img/c1.png)

### ServerChan

We Use [Server Chan](http://sc.ftqq.com/) to realize its functionality. For its configuration method, please refer to its documentation (In Chinese).

Then, you just need to follow the [Usage](#Usage) step 1 to create an Actions Secret whose name is `SERVERCHANSCKEY` and value is [Your SCKEY](http://sc.ftqq.com/?c=code). Then the workflow can automatically push the relevant information of the automatic health reporting results for you.

*Effect Graphs*：

Pushing Effect：
![](img/ServerChan.jpg)

Details：
![](img/ServerChanMessage.jpg)

### ServerChan Testing Subscription Version

If you want to use [ServerChan Testing Subscription Version](https://sct.ftqq.com/), please create/modify the Actions secret with the Name `SERVERCHANSCKEY` and the value [your sendkey value](https://sct.ftqq.com/sendkey). In addition, create a Actions secret with Name as `OPENID`, if the value is `0`, it is only send to yourself. Otherwise, set the value to be the specified user's Wechat openid who subscribed the Testing Subscription account, then it will send it to the designated user and yourself at the same time.

If you need to switch back to normal SeverChan, please delete the `OPENID` actions secret.

## Self-Configure Workflow

You can create your own repository and configure your own workflow to use, [Example Workflow YAML File](.github/workflows/autoreport-docker.yml)

### Input

#### Required

* CARDID: Your Student Card ID
* PASSWORD: Your Student Email Login Password

#### Optional

* DELAYS: Delay time for running
* SERVERCHANSCKEY: ServerChan SCKEY
* OPENID: ServerChan Testing Subscription Version Testing Subscription account User OpenID
* PPTOKEN: PushPlus Token
* PPTOPIC: PushPlus Topic

### Example

```yaml
- name: Auto COVID Health Report
  uses: HollowMan6/LZU-Auto-COVID-Health-Report@master
  with:
    CARDID: ${{ secrets.CARDID }}
    PASSWORD: ${{ secrets.PASSWORD }}
    DELAYS: ${{ github.event.inputs.delays }}
    SERVERCHANSCKEY: ${{ secrets.SERVERCHANSCKEY }}
    OPENID: ${{ secrets.OPENID }}
    PPTOKEN: ${{ secrets.PPTOKEN }}
    PPTOPIC: ${{ secrets.PPTOPIC }}
```

## Docker

Docker Hub: https://hub.docker.com/r/hollowman6/lzu-auto-covid-health-report

If you need to run through docker, just set the above Actions Secrets name and value as environment variables (In addition, add a DELAYS as the waiting time, and the value is the same requirement as that in step 6 of [usage](#usage)), and then execute the following command:

```bash
docker run -it \
    -e CARDID=$CARDID \
    -e PASSWORD=$PASSWORD \
    -e DELAYS=$DELAYS \
    -e SERVERCHANSCKEY=$SERVERCHANSCKEY \
    -e OPENID=$OPENID \
    -e PPTOKEN=$PPTOKEN \
    -e PPTOPIC=$PPTOPIC \
    -e DELAYS=$DELAYS \
    hollowman6/lzu-auto-covid-health-report
```

**Build**

```bash
docker build -t hollowman6/lzu-auto-covid-health-report .
```

The docker image here can also be runned in combination with Kubernetes' CronJob in the Cloud Clusters etc. THere're unlimited possibilities.

## Q&A

*PS:* If you want to use crontab on your own Linux server to execute the auto Health Report, I recommend using [docker](#docker), otherwise please clone this repository and after installing relevant Python dependencies, adapt the path of the python program in [entrypoint.sh](entrypoint.sh). Set the Actions Aecrets name and value mentioned above as the environment variable respectively (In addition, add a DELAYS as the waiting time, and the value is the same requirement as that in step 6 of [usage](#usage)) to run.

1. How to check whether you have reported your health successfully?

If you are referring to the health reporting system in the Lanzhou University APP, please cancel the "whether the staff are in Lanzhou (whether the students are in school)" column and then report manually. After successfully reported, again open the app and you will be prompted "当日填报完成，如变化请更新！".

If you are referring to GitHub actions, please check the running record directly. If there is no error in workflow, the reporting is successful. If it fails, GitHub will send a message to prompt workflow to fail.


Of course, you can also configure to use [SeverChan Wechat push](#optional-wechat-push-results).

2. There is no temperature option you gave in reporting system

When returning to school, if the university still wants to report three times a day, there will be.

You don't need to report your temperature three times a day during the holidays. This function is for the future when you go back to school. My program will automatically determine whether you are currently in school or not. If you are not in school, there will be no valid temperature data (all 0.0). In addition, these items are required for every post data.

And also, GitHub actions is set to run the program three times a day. If you don't need it, you can replace [here](
https://github.com/HollowMan6/LZU-Auto-COVID-Health-Report/blob/main/.github/workflows/autoreport.yml#L10)
with `    - cron: '0 23 * * *' # Schedule on CST 7 everyday`，
That is, only runs at 7 a.m. Beijing time every day.

**Warning**:

***For TESTING ONLY, not for any ILLEGAL USE!***

***I will not be responsible for any adverse consequences caused by using this code.***
