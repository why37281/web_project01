import flask
app = flask.Flask(__name__)
@app.route('/')
def web():
    return '<a src="#">主页</a>'
if __name__ == '__main__':
    app.run()