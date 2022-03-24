FROM python:3.7-slim
RUN apt-get update
RUN apt-get -y install gcc
COPY . /usr/app/
EXPOSE 4002
WORKDIR /usr/app/
RUN pip install -r requirements.txt
CMD python3.7 main.py

