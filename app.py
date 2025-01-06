from flask import Flask, request
from telegram import Bot
from telegram.ext import Dispatcher
from telegram.ext import Application
import os

# Initialize Flask app
app = Flask(__name__)

# Bot setup
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = Bot(token=TOKEN)
application = Application.builder().bot(bot).build()

# Webhook route
@app.route('/webhook', methods=['POST'])
def webhook():
    json_str = request.get_data(as_text=True)
    update = Update.de_json(json_str, bot)
    application.update_queue.put(update)  # Process the update
    return 'OK', 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
