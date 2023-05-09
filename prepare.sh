#!/bin/bash

# function run_docker {
#     docker-compose -f docker/docker-compose.local.yml run --rm web $@
# }

# Resets the local Django database, adding an admin login and migrations
set -e

echo -e "\n>>> Removing migrations"
find ./smartcitycard -path "*/migrations/*.py" -not -name "__init__.py" -delete
find ./smartcitycard -path "*/migrations/*.pyc"  -delete
find ./accounts -path "*/migrations/*.py" -not -name "__init__.py" -delete
find ./accounts -path "*/migrations/*.pyc"  -delete
find ./card -path "*/migrations/*.py" -not -name "__init__.py" -delete
find ./card -path "*/migrations/*.pyc"  -delete
find ./magala -path "*/migrations/*.py" -not -name "__init__.py" -delete
find ./magala -path "*/migrations/*.pyc"  -delete
find ./core -path "*/migrations/*.py" -not -name "__init__.py" -delete
find ./core -path "*/migrations/*.pyc"  -delete
find ./cities -path "*/migrations/*.py" -not -name "__init__.py" -delete
find ./cities -path "*/migrations/*.pyc"  -delete


echo -e "\n>>> Resetting the database"
python manage.py reset_db --close-sessions --noinput

echo -e "\n>>> Running migrations"
python manage.py makemigrations


echo -e "\n>>> Copy cities latest migrations"
cp ./cities/bak/continents_import.py ./cities/migrations/0003_continents_import.py

echo -e "\n>>> Running migrations"
python manage.py migrate

echo -e "\n>>> Importing cities"
python manage.py cities --import=country
# python manage.py cities --import=region
# python manage.py cities --import=subregion

echo -e "\n>>> Creating new superuser 'admin'"
python  manage.py createsuperuser \
   --username admin \
   --email admin@example.com \
   --noinput

echo -e "\n>>> Setting superuser 'admin' password to 12345"
python manage.py shell_plus --quiet-load -c "
u=User.objects.get(username='admin')
u.set_password('password')
u.save()
"

# Any extra data setup goes here.

echo -e "\n>>> Database restore finished."