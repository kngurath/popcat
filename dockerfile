FROM python:alpine

ENV TZ=Asia/Taipei
WORKDIR /data

COPY requirements.txt  requirements.txt
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
