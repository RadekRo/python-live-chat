from flask import Flask, render_template, url_for, request, jsonify, session, redirect
import mimetypes
import bcrypt

mimetypes.add_type('application/javascript', '.js')
app = Flask(__name__)
app.secret_key = bcrypt.gensalt()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/chat", methods = ["POST", "GET"])
def chat():
    if request.method == "POST":
        user = request.form.get('user-name')
        session['username'] = user
        return redirect('/chat')
    else:
        return render_template('chat.html')

@app.route("/chat/add_message", methods = ["GET", "POST"])
def add_message():
    message = request.json['messageInputText']
    user = session.get('username')
    data = {'data': message, 'user': user}
    return jsonify(data)


if __name__ == '__main__':
    app()
