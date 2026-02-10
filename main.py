from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>This is paragraph!</p>'
            '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWZsOXV0bTJla3VpMXR3NGc0ZWJ4YzBuMjYycnhnbGR1eW1lbDQyeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4Iw2OzgiiTc4M/giphy.gif" width=200>')

@app.route("/buy")
def say_buy():
    return "Buy!"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f'Hello {name}, you are {number} years old!'

if __name__ == '__main__':
    app.run(debug=True)