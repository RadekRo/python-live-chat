from flask import Flask, render_template, url_for, request, jsonify, session, redirect, datetime
import mimetypes
import bcrypt
from data import queries

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
            if session.get('username'):
                return render_template('chat.html', username = session.get('username'))
            else:
                print('Error. Operation forbidden!')
                return render_template('index.html')
        
@app.route("/chat/add_message", methods = ["GET", "POST"])
def add_message():
    message = request.json['messageInputText']
    user = session.get('username')
    date_and_time = datetime.now().strftime('%Y-%m-%d %H:%M')
    queries.add_message(message, user, date_and_time)
    data = {'data': message, 'user': user}
    return jsonify(data)


if __name__ == '__main__':
    app()
