# Dockerfile for multi-stage build.
# Will be used by CI to generate final image.

FROM node:20.14

RUN apt-get update && apt-get -y upgrade

WORKDIR /project
COPY ./ /project

RUN yarn install --frozen-lockfile
RUN yarn build


FROM python:3.12

ENV APP_ENV production
ENV PORT 8000
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y --no-install-recommends \
    gettext \
    netcat-traditional \
    texlive

# Copy docker entrypoint script to appropriate location, give execute
# permissions.
COPY docker/app/entrypoint.production.sh /usr/local/sbin/entrypoint.sh
RUN chmod a+x /usr/local/sbin/entrypoint.sh

COPY docker/app/gunicorn.conf.py /etc/

COPY --from=0 /project /project

WORKDIR /project

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir --requirement requirements.txt
RUN python manage.py compilemessages
# RUN python manage.py collectstatic --noinput

EXPOSE 8000

ENTRYPOINT ["/usr/local/sbin/entrypoint.sh"]
CMD ["gunicorn", "app.wsgi", "--config", "/etc/gunicorn.conf.py", "--log-level", "debug"]
