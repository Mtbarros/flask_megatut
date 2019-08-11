#!/usr/bin/python3

# use this to create local server at localhost:5000

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
    app.run()
except Exception as e:
    print('Problem in main with app.run():', e)
    exit(-1)