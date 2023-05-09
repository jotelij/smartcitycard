# Pull base image
FROM python:3.11-slim-buster

#arguments
# ARG app_debug=True # <- this one's new

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
###
# ENV APP_DEBUG=$app_debug

# gdal for GeoDjango
RUN apt-get update && apt-get install -y \
    binutils \
    gdal-bin \
    libproj-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /code/backend

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Install cities dependencies
# COPY ./django_cities-0.6.1-py3-none-any.whl .
# RUN pip install django_cities-0.6.1-py3-none-any.whl

# Copy project
COPY . .

# set work directory
WORKDIR /code/backend
# RUN python manage.py makemigrations
# RUN python manage.py migrate
# RUN python manage.py migrate cities
# CMD ["python", "manage.py", "makemigrations", "--no-input"]
# CMD ["python", "manage.py", "migrate", "--no-input"]