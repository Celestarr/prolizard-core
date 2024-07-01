FROM python:3.12

ENV APP_ENV development
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y --no-install-recommends \
    gettext \
    netcat-traditional \
    texlive

# Copy docker entrypoint script to appropriate location, give execute
# permissions.
COPY docker/app/entrypoint.development.sh /usr/local/sbin/entrypoint.sh
RUN chmod a+x /usr/local/sbin/entrypoint.sh

WORKDIR /project

EXPOSE 8000

ENTRYPOINT ["/usr/local/sbin/entrypoint.sh"]
CMD ["python" ,"manage.py", "runserver", "0.0.0.0:8000"]
