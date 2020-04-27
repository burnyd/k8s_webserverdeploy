FROM ubuntu:18.04

WORKDIR /tmp/

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY  . /tmp

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]


