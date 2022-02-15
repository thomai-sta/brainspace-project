FROM ubuntu:18.04


RUN apt update && apt install -y software-properties-common gcc && \
    add-apt-repository -y ppa:deadsnakes/ppa
RUN apt update && apt install -y python3.6 python3-distutils python3-pip python3-apt
RUN apt install -y git

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY ./dist/dictionary-1.0.0-py3-none-any.whl /app/dictionary-1.0.0-py3-none-any.whl

RUN pip3 install dictionary-1.0.0-py3-none-any.whl
ENV FLASK_APP=dictionary

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN flask init-db

RUN pip3 install waitress
CMD waitress-serve --call 'dictionary:create_app'