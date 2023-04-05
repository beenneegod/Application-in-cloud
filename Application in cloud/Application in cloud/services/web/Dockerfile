FROM python:3.10.7-slim-buster
WORKDIR /services/web

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat

RUN pip install --upgrade pip
COPY ./requirements.txt /services/web/requirements.txt
RUN pip install -r requirements.txt

COPY . /services/web/

RUN chmod +x /services/web/entrypoint.sh
ENTRYPOINT ["/services/web/entrypoint.sh"]