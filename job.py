#!/usr/bin/env python
# -*-coding:utf-8-*-
# by 'hollowman6' from Lanzhou University(兰州大学)

import os


def job_function():
    failure = False
    if os.system("python LZU-Auto-COVID-Health-Report.py delayrand >> information.txt && cat information.txt >> logs.txt && cat information.txt") == 0:
        if os.system("python Notify-Result.py success") != 0:
            failure = True
    else:
        failure = True
        os.system(
            "python Notify-Result.py failure && cat information.txt >> logs.txt && cat information.txt")
    delays = os.environ['DELAYS']
    os.system("rm information.txt")
    if failure and delays:
        os.system("echo 'Sleep for " + delays +
                  " and the health report will start again!'")
        os.system("echo 'Sleep for " + delays +
                  " and the health report will start again!' >> logs.txt")
        os.system("sleep " + delays)
        job_function()


if __name__ == "__main__":
    job_function()
