from flask import Flask, render_template, request
import threading
from bot import run_bot

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ""
    if request.method == 'POST':
        user_input = request.form['message']
        response = f".start {user_input}"
    return render_template('index.html', response=response)

# Run Guilded bot in a separate thread
threading.Thread(target=run_bot).start()

if __name__ == '__main__':
    app.run()
