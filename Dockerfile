FROM python:3.9.5-slim-buster
# https://github.com/docker-library/repo-info/blob/master/repos/python/remote/3.9.5-slim-buster.md#python395-slim-buster

# FROM jupyter/pyspark-notebook:ubuntu-20.04

LABEL MAINTAINER = "Frederico Horst <https://github.com/fredericohorst>"

COPY requirements-lite.txt .

RUN apt-get update

RUN pip3 install --upgrade --no-cache-dir -r requirements.txt

RUN mkdir /leitor-arquivos

WORKDIR /leitor-arquivos

COPY . . 

CMD [ "python3", "main.py" ]
