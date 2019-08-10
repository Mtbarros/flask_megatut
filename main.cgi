#!/usr/bin/python3

# import CGI handler
from wsgiref.handlers import CGIHandler

# try to import actual flask code
app = None
try:
    import megatut_app
    app = megatut_app.app
except Exception as e:
    print('Problem in main with megatut_app import:', e)
    exit(-1)

# create a wrapper around app that fills it with the needed environment for CGI shared webhosting
class EnvironApp(object):
   def __init__(self, app):
       self.app = app
   def __call__(self, environ, start_response):
       environ['SERVER_NAME'] = ""
       environ['SERVER_PORT'] = "80"
       environ['REQUEST_METHOD'] = "GET"
       environ['SCRIPT_NAME'] = ""
       environ['PATH_INFO'] = "/"
       environ['QUERY_STRING'] = ""
       environ['SERVER_PROTOCOL'] = "HTTP/1.1"
       return self.app(environ, start_response)


app = EnvironApp(app)

# try to run flask app
try:
    CGIHandler().run(app)
except Exception as e:
    print('Problem in main with CGIHandler().run(app):', e)
    exit(-1)
