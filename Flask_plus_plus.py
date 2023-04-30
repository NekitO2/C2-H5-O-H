from flask import Flask
from flask import render_template

link = 'http://127.0.0.1:5000/'
app = Flask(__name__)

@app.route('/')

def first():
    return render_template('index.html')

@app.route('/2')

def second():
    return render_template('test_button.html')

@app.route('/telegram_bot')
def telegram_bot():
    return render_template('telegram_bot.html')
app.run()           