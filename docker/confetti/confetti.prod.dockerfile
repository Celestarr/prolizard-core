# Dockerfile for multi-stage build.
# Will be used by CI to generate final image.

FROM node:16.12.0-bullseye

RUN apt-get update && apt-get -y upgrade

WORKDIR /project
COPY ./ /project

RUN yarn install --frozen-lockfile
RUN yarn build

FROM python:3.9.7-bullseye

ENV PORT 9901
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y texlive-core gettext

# Copy docker entrypoint script to appropriate location, give execute
# permissions.
COPY docker/confetti/entrypoint.prod.sh /usr/local/sbin/entrypoint.sh
RUN chmod a+x /usr/local/sbin/entrypoint.sh

COPY docker/confetti/gunicorn.prod.conf.py /etc/gunicorn.conf.py

COPY --from=0 /project ./

WORKDIR /project/

RUN python -m pip install --upgrade pip
RUN pip install --requirement requirements.txt

EXPOSE 9901

ENTRYPOINT ["/usr/local/sbin/entrypoint.sh"]
