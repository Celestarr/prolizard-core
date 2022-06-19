FROM python:3.9.7-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y texlive gettext

# Copy docker entrypoint script to appropriate location, give execute
# permissions.
COPY docker/seoul/entrypoint.dev.sh /usr/local/sbin/entrypoint.sh
RUN chmod a+x /usr/local/sbin/entrypoint.sh

WORKDIR /project

EXPOSE 8000

ENTRYPOINT ["/usr/local/sbin/entrypoint.sh"]
CMD ["python" ,"manage.py", "runserver", "0.0.0.0:8000"]
