from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/buy")
def say_buy():
    return "buy"

if __name__ == '__main__':
    app.run()