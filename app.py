from flask import Flask, render_template, url_for, request
import mimetypes

mimetypes.add_type('application/javascript', '.js')
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/chat")
def chat():
    return render_template('chat.html')

@app.route("/chat/add_message")
def add_message():
    message = request.form.get('message')


if __name__ == '__main__':
    app()
