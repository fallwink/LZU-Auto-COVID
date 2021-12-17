下面使用Linux（Ubuntu、Centos之流都是Linux）服务器环境来进行兰州大学健康打卡程序运行配置的讲解。

现在可以直接用`git`克隆[gitee](https://gitee.com/hollowman6/LZU-Auto-COVID-Health-Report)上的仓库，现假设你要把仓库放在你的家目录的gitee文件夹下(`~/gitee`)，执行：

```bash
mkdir -p ~/gitee
cd ~/gitee
git clone https://gitee.com/hollowman6/LZU-Auto-COVID-Health-Report
```

安装一下python依赖：

```bash
cd ~/gitee/LZU-Auto-COVID-Health-Report
pip install -r requirements.txt
```

然后假设你要把执行脚本放在家目录下（`~`），名称为`LZU-Auto-COVID-Health-Report.sh`，执行：

```bash
cd ~
nano LZU-Auto-COVID-Health-Report.sh
```
这样就会打开nano编辑器，将以下内容复制粘贴到输入区域，把`Setup Environmental Variables`部分必填的账号和密码中`替换成你的XX`字样改成自己的对应信息，其它选填项可类似在引号中间自行选择填写，作为执行脚本内容（变量的含义可以参考[仓库README说明](https://gitee.com/hollowman6/LZU-Auto-COVID-Health-Report#%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95)）：

```bash
#!/usr/bin/env bash

# Setup Environmental Variables
cd ~/gitee/LZU-Auto-COVID-Health-Report
echo "export CARDID='替换成你的账号'" >> envar
echo "export PASSWORD='替换成你的密码'" >> envar
echo "export PPTOKEN=''" >> envar
echo "export PPTOPIC=''" >> envar
echo "export SERVERCHANSCKEY=''" >> envar
echo "export TGBOTTOKEN=''" >> envar
echo "export TGCHATID=''" >> envar
SUBSINFO=''
echo "export SUBSINFO='$SUBSINFO'" >> envar
echo "export CORPID=''" >> envar
echo "export CORPSECRET=''" >> envar
echo "export AGENTID=''" >> envar
echo "export DELAYS='30m'" >> envar

command=""
if [ -f "envar" ]; then
    command=$command"source envar && "
    command=$command"rm envar && "
fi
command=$command"python job.py"

# Main Program Execution
eval "$command"
```
运行脚本到这里就构建完成了，键盘`Ctrl-o`写入，回车`Enter`确认文件名，`Ctrl-x`退出`nano`。

然后更改文件可执行权限：
```bash
chmod +x LZU-Auto-COVID-Health-Report.sh
```

随后手动运行一下看看是否能打卡成功（会有0-20分钟打卡时间延迟，做好等待准备）:
```bash
./LZU-Auto-COVID-Health-Report.sh
```
![](https://img-blog.csdnimg.cn/6d77c590bde9455381e508d5d33f42ec.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBASG9sbG93TWFuNg==,size_20,color_FFFFFF,t_70,g_se,x_16)

无报错且成功退出则代表配置一切正常！否则请检查确认错误原因。

随后使用CronTab配置定时运行（默认系统可能没有安装CronTab软件，如下面步骤命令提示找不到`crontab`命令请根据你的Linux发行版（Ubuntu或Centos等）参考[这篇博客](https://blog.csdn.net/longgeaisisi/article/details/90477975)进行安装配置，也可自行百度搜索安装方法）

```bash
crontab -e
```

在编辑区，增加输入下面内容设定为每天7点半自动打卡，然后保存并退出：
```bash
30 7 * * * ~/LZU-Auto-COVID-Health-Report.sh
```

大功告成！
