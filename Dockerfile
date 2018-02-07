# Build
# docker build -t "thevoice:develop" .
FROM python:3.6

# Set work directory
WORKDIR /usr/src/app
COPY . .
RUN chmod +x entrypoint.sh

# This value is used in django settings
# TODO: Find a better way to do the same
ENV DOCKER_CONTAINER=true

# Install dependency manager
# and project dependencies
RUN pip install pipenv==9.0.3
RUN pipenv install
