from functools import wraps

import gunicorn.http.wsgi

chdir = "/htdocs/www/src"

bind = "0.0.0.0:20000"

# user = "www-data"
# group = "www-data"

workers = 1
worker_class = "gevent"

graceful_timeout = 60


def wrap_default_headers(func):
    @wraps(func)
    def default_headers(*args, **kwargs):
        return [header for header in func(*args, **kwargs) if not header.startswith('Server: ')]
    return default_headers


gunicorn.http.wsgi.Response.default_headers = wrap_default_headers(gunicorn.http.wsgi.Response.default_headers)
