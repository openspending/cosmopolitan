.PHONY: help

.DEFAULT_GOAL := help

REPOSITORY := 'openspending/cosmopolitan'
SHELL := /bin/bash

help: # http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

install: ## install the dependencies for the app
	pip3 install --upgrade pip
	pip3 install --upgrade --no-cache-dir --exists-action w -r requirements.txt

release: ## tag a release from master and push to origin
	bash -c '[[ -z `git status -s` ]]'
	git tag -a -m release $(VERSION)
	git push --tags

test: ## run the tests for the app
	python3 manage.py test

build: ## build the Docker image for this app
	docker build --tag $(REPOSITORY) --rm=false .

login: ## Login to docker hub
	docker login -e $DOCKER_EMAIL -u $DOCKER_USER -p $DOCKER_PASSWORD

push: ## push the latest Docker image to DockerHub
	docker push $(REPOSITORY)

shell: ## run an interactive bash session in the container
	docker run -it $(REPOSITORY) /bin/bash

run: ## run the container
	docker run $(REPOSITORY)

deploy: build login push

migrate: ## run database migrations for the app
	python3 manage.py migrate --no-input

server: ## command to run the server
	gunicorn application.wsgi --config server.py
