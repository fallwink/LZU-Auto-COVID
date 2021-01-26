FROM python:latest

MAINTAINER Hollow Man <hollowman@hollowman.ml>

LABEL version="1.0.1"
LABEL repository="https://github.com/HollowMan6/LZU-Auto-COVID-Health-Report"
LABEL homepage="https://hollowman.ml/"
LABEL maintainer="Hollow Man <hollowman@hollowman.ml>"

COPY entrypoint.sh /entrypoint.sh
COPY LZU-Auto-COVID-Health-Report.py /LZU-Auto-COVID-Health-Report.py
COPY Notify-Using-SeverChan-Or-PushPlus.py /Notify-Using-SeverChan-Or-PushPlus.py
COPY requirements.txt /requirements.txt

ENV TZ Asia/Shanghai

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
