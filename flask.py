from gevent import monkey
monkey.patch_all()
from flask import Flask
from gevent import pywsgi

print('success')


app = Flask(__name__)
def cal(x):
    return x**2+2*x+x/10

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    a = int(name)
    result = cal(a)
    return '<h1>Hello, %s!</h1>' % result

if __name__ == '__main__':
    server = pywsgi.WSGIServer(('127.0.0.1', 5000), app)
    server.serve_forever()

    #app.run(debug=True)
#    app.run(host='0.0.0.0',port=9000,debug=True)



