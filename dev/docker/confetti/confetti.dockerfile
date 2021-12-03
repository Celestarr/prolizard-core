FROM python:3.9.7-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y gettext

# Copy docker entrypoint script to appropriate location, give execute
# permissions.
COPY dev/docker/confetti/entrypoint.sh /usr/local/sbin/
RUN chmod a+x /usr/local/sbin/entrypoint.sh

WORKDIR /confetti/

ENTRYPOINT ["/usr/local/sbin/entrypoint.sh"]
