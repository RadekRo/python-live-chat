from flask import Flask, render_template, url_for, request, jsonify
import mimetypes

mimetypes.add_type('application/javascript', '.js')
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/chat")
def chat():
    return render_template('chat.html')

@app.route("/chat/add_message", methods = ["GET", "POST"])
def add_message():
    message = request.json['messageInputText']
    print(message)
    data = {'data': message}
    return jsonify(data)


if __name__ == '__main__':
    app()
