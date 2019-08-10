from megatut_app import app

@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World1!'

@app.route('/ola')
def ola():
    return 'OLA!'
