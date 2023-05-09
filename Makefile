FRONTEND ?= frontend
NAME ?= backend
RUN = docker-compose exec $(NAME)

starte:
	docker-compose up -d

start:
	docker-compose up -d --build

stop:
	docker-compose down

run:
	$(RUN) manage.py runserver  0.0.0.0:8000

mig:
	$(RUN) python manage.py migrate

migcities:
	$(RUN) python manage.py migrate cities

mm:
	$(RUN) python manage.py makemigrations
	$(RUN) python manage.py migrate

res:
	$(RUN) bash prepare.sh

inco:
	$(RUN) python manage.py cities --import=country

# .PHONY: all start run-inside stop