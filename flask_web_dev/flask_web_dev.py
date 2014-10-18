from flask import Flask, request, current_app

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

if __name__ == '__main__':
    app.run(debug=True)
