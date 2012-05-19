from bottle import Bottle, run

app = Bottle()

@app.route('/')
def index():
    return 'Index page'

@app.route('/hello')
def hello():
    return 'Hello world!'

@app.get('/api')
def api():
    return {'key':'value'}

run(app, host='localhost', port=8080)
