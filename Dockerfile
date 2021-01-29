FROM python:slim

MAINTAINER Hollow Man <hollowman@hollowman.ml>

LABEL version="1.0.5"
LABEL repository="https://github.com/HollowMan6/LZU-Auto-COVID-Health-Report"
LABEL homepage="https://hollowman.ml/"
LABEL maintainer="Hollow Man <hollowman@hollowman.ml>"

COPY entrypoint.sh /entrypoint.sh
COPY LZU-Auto-COVID-Health-Report.py /LZU-Auto-COVID-Health-Report.py
COPY Notify-Using-SeverChan-Or-PushPlus.py /Notify-Using-SeverChan-Or-PushPlus.py
COPY requirements.txt /requirements.txt

ENV TZ Asia/Shanghai

RUN apt-get update \
    && apt-get install -y \
      libxml2 \
      libxslt1-dev \
      gcc \
      zlib1g-dev \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /requirements.txt \
    && chmod +x /entrypoint.sh \
    && apt-get --purge remove -y \
      libxml2 \
      gcc \
      zlib1g-dev \
    && apt-get autoremove -y \
    && apt-get clean

ENTRYPOINT ["/entrypoint.sh"]
