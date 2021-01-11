
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

(English version is down below)

[Python库依赖](../../network/dependencies)

[自动打卡脚本](LZU-Auto-COVID-Health-Report.py)

[工作流](.github/workflows/autoreport.yml)

## 使用方法

（强烈建议你首先自己打一次卡之后再使用本软件，从而初始化平台打卡系统中的数据，本软件将会一直沿用你最新填报的打卡信息。如果需要更改打卡数据，请自己手动在填报平台任意时间段填报一次最新的信息就好）

你可以首先fork本仓库，之后在你fork的仓库中进行相关设置。

1. 首先，按下图所示点击1，2，3的次序，进入新建Actions secrets的界面。我们需要两个Actions secrets，一个的Name为`CARDID`，value为你的兰州大学校园卡号；另一个的Name为`PASSWORD`，value为你的兰州大学个人工作台的账户密码。依次按上述要求创建这两个secrets即可。创建完成后你将在右下部分看到两个Actions secrets。
![](img/secrets.png)

2. 然后，按下图所示点击1，2，3，4的次序，你可以手动触发工作流的执行来进行测试。（**注意：**：如果因为你多次重复因为账号密码错误登录失败，会导致验证码的出现，此时程序会被阻止自动登录。因而请确保你已经在[兰州大学个人工作台](http://my.lzu.edu.cn:8080/login?service=http://my.lzu.edu.cn)处测试过你的账号密码是正确的。）另外工作流还自动会在北京时间每天的7点，11点，19点自动运行。
![](img/workflow.png)

3. 点开任意一个运行记录，依次点开下图所示1，2，你可以看到运行记录以及错误说明。
![](img/run.png)

4. 如果某次因为某些因素工作流运行失败，GitHub会自动发邮件提醒工作流运行失败，从而方便自己手动打卡。

5. 将来某一天疫情过去了，不需要再打卡，你可以按下图操作关闭：
![](img/cancel.png)


**警告**：

***仅供测试使用，不可用于任何非法用途！***

***对于使用本代码所造成的一切不良后果，本人将不负任何责任！***
# LZU Auto COVID Health Report using Github Action

[Python library dependency](../../network/dependencies)

[Auto Report Script](LZU-Auto-COVID-Health-Report.py)

[Workflow](.github/workflows/autoreport.yml)

## Usage

(It is strongly recommended that you first report your own situation by yourself before using this software so that the system's data can be initialized. This software will always use the data you keep in the system. If you need to change the reporting data, please manually fill in your latest information at any time in the reporting platform.)

You can fork this repository first, and then set related settings in your forked repository.

1. First, click in the order of 1, 2 and 3 as shown in the figure below to enter creating the new actions secrets interface. We need two actions secrets, one name is `CARDID`, value is your student card number of Lanzhou University; the other is `PASSWORD`, value is the account password of your personal workbench of Lanzhou University. Create these two secrets in turn according to the above requirements. After the creation, you will see two actions secrets as in the lower right section.
![](img/secrets.png)

1. Then, click in the order of 1, 2, 3 and 4 as shown in the figure below. You can manually trigger the execution of workflow to test. (**Note:**: if you repeatedly fail to log in because of the wrong account or password, the program will be prevented from logging in automatically by reCAPTCHA. So please make sure that you can successfully logged into [Lanzhou University personal workbench](http://my.lzu.edu.cn:8080/login?service=http://my.lzu.edu.cn) with your account number and password and that they are correct.) In addition, the workflow will automatically run at 7:00, 11:00 and 19:00 Beijing time every day.
![](img/workflow.png)

3. Click any running record, and then click in the order of 1 and 2 as shown in the figure below. You can see the running record and error description.
![](img/run.png)

4. If the workflow fails due to some errors, GitHub will automatically send an email to remind the workflow of failure, so on receiving this, you can report by yourself.

5. One day, when the COVID-19 is over, and you don't need to report your health any more. You can disable it according to the following figure:
![](img/cancel.png)

**Warning**:

***For TESTING ONLY, not for any ILLEGAL USE!***

***I will not be responsible for any adverse consequences caused by using this code.***
