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

# try to run flask app
try:
    CGIHandler().run(app)
except Exception as e:
    print('Problem in main with CGIHandler().run(app):', e)
    exit(-1)
