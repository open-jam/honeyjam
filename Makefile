.PHONY: all help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# docker
docker-cmd: install-package settings run-server
docker-uwsgi-cmd: install-package migrate run-uwsgi
docker-gunicorn-cmd: install-package migrate run-gunicorn


# install
settings:
	@pipenv run make settings-internal

settings-internal:
	@cd src && python -m scripts.generate_secret -a default

install-mysql:
	@apt update && apt install -y mysql-server default-libmysqlclient-dev

install-package:
	@pipenv install --dev

migrate:
	@pipenv run python src/manage.py migrate

certs:
	@mkcert -install
	@rm -rf docs/dev/cert && mkdir docs/dev/cert && cd docs/dev/cert && mkcert -key-file key.pem -cert-file cert.pem honeyjam.local '*.honeyjam.local'

# build
build: collect-static

collect-static:
	@pipenv run python src/manage.py collectstatic --no-input --clear


# run
run-front:
	@yarn start

run-server:
	@pipenv run python src/manage.py runserver 0.0.0.0:20000

run-uwsgi:
	@pipenv run uwsgi --ini /htdocs/www/docs/wsgi/uwsgi/django.ini --import infras.crontab

run-gunicorn:
	@pipenv run gunicorn -c /htdocs/www/docs/wsgi/gunicorn/django.py sites.wsgi:application

shell:
	@pipenv shell

# test
test:
	@pipenv run python src/manage.py test src --noinput --settings=sites.settings.test

# pre-processing
lint:
	@pipenv run autopep8 --exclude migrations --in-place --aggressive --recursive ./src/
	@pipenv run pylint ./src/ --rcfile=.pylintrc
	@pipenv run flake8

# docker
docker-up:
	@docker-compose up

docker-rebuild-up:
	@docker-compose up --force-recreate --build

docker-kill-all:
	@docker ps -a -q | xargs docker rm -f
