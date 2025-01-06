from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    update = request.json
    # Handle incoming Telegram updates
    print("Received update:", update)
    return "OK"
