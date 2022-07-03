FROM python:3.10-buster

RUN useradd --create-home --shell /bin/bash app_user

WORKDIR /home/app_user

COPY . .

RUN apt-get install libpq-dev
RUN pip install -r requirements.txt

USER app_user

EXPOSE 8000
