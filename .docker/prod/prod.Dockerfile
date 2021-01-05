# Start with the python 3 image from docker hub
FROM python:3

LABEL maintainer="cyee@bscs.org" description="Python Flask server for handling Snipcart webhook requests."

# Copy all files in current directory into the /app directory inside the container
COPY /app /app

COPY Pipfile /app
COPY Pipfile.lock /app

# Set our working directory
WORKDIR /app

# Upgrade pip
RUN ["pip", "install", "--no-cache-dir", "--upgrade", "pip==18.0"]

# Install pipenv
RUN ["pip", "install", "--no-cache-dir", "pipenv"]

# Install app dependencies at the containers system level, include dev dependencies for our dev environment
RUN ["pipenv", "install", "--system", "--deploy"]

# Update apt-get
RUN ["apt-get", "update"]
