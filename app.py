from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'data-v2'


if __name__ == "main":
    app.run()
