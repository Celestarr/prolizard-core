# pylint: disable=invalid-name

import multiprocessing

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
# access_logfile = "/var/log/myfolab_api/gunicorn.log"
# error_logfile = "/var/log/myfolab_api/gunicorn.err.log"
