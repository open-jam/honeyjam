FROM python:3.8

RUN pip3 install pip --upgrade \
    && pip3 install pipenv

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /htdocs/www
WORKDIR /htdocs/www

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --dev

EXPOSE 13000
