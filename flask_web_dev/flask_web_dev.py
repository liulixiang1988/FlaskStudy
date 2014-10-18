from flask import Flask, request, current_app, make_response

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! %s' % current_app.name, 404


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s</h1>' % name


@app.route('/browser')
def browser():
    user_agent = request.headers.get('User-Agent')
    return '<p>你的浏览器是：%s' % user_agent


@app.route('/mp')
def mp():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

from flask import redirect


@app.route('/redirect_demo')
def redirect_demo():
    return redirect('http://www.baidu.com')

if __name__ == '__main__':
    app.run(debug=True)
