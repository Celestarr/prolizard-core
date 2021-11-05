import multiprocessing

bind = "0.0.0.0:9901"
workers = multiprocessing.cpu_count() * 2 + 1
# access_logfile = "/var/log/myfolab_api/gunicorn.log"
# error_logfile = "/var/log/myfolab_api/gunicorn.err.log"
