FROM ubuntu:18.04

RUN apt-get update && \
    apt-get -y install python3 python3-pip

ADD ./app/ /app/

RUN python3 -m pip install -r /app/requirements.txt

EXPOSE 80

CMD python3 /app/app.py
