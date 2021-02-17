#!/usr/bin/env python
# -*-coding:utf-8-*-
# by 'hollowman6' from Lanzhou University(兰州大学)

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import os


def job_function():
    failure = False
    if os.system("python LZU-Auto-COVID-Health-Report.py >> information.txt && cat information.txt >> logs.txt") == 0:
        if os.system("python Notify-Result.py success >> logs.txt") != 0:
            failure = True
    else:
        failure = True
        os.system(
            "python Notify-Result.py failure >> logs.txt && cat information.txt >> logs.txt")
    delays = os.environ['DELAYS']
    if failure and delays:
        os.system("echo 'Sleep for " + delays +
                  " and the health report will start again!")
        os.system("sleep " + delays)
        job_function()


sched = BlockingScheduler()
sched.add_job(job_function, CronTrigger.from_crontab(os.environ['CRONEXP']))
sched.start()
