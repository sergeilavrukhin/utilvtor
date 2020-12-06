FROM python:3.6.8-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

RUN apk update && apk --no-cache add gcc musl-dev libxslt-dev python3-dev bash nano mc htop bzip2 tzdata postgresql-dev

COPY Pipfile /

RUN pip install --upgrade pip \
  && pip3 install pipenv  httpie\
  && pipenv lock\
  && pipenv install --deploy --system  --ignore-pipfile

COPY src/flask/ /code/
EXPOSE 5000