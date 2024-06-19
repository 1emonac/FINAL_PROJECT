# pull official base image
FROM python:3.10-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# copy requirements file first
COPY requirements.txt /usr/src/app/

# install dependencies with additional options
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# copy project files to the container
COPY . /usr/src/app/
