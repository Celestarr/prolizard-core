FROM python:3.9.7-bullseye

ENV PORT 9901
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y gettext

# Copy docker entrypoint script to appropriate location, give execute
# permissions.
COPY docker/scripts/entrypoint.prod.sh /usr/local/sbin/entrypoint.sh
RUN chmod a+x /usr/local/sbin/entrypoint.sh

COPY docker/configs/gunicorn.prod.conf.py /etc/gunicorn.conf.py

COPY . /confetti/

WORKDIR /confetti/

RUN python -m pip install --user --upgrade pip
RUN pip install --requirement requirements.txt

WORKDIR /confetti/app/

EXPOSE 9901

ENTRYPOINT ["/usr/local/sbin/entrypoint.sh"]
