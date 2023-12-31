from flask import Flask, render_template, url_for, request, jsonify, session, redirect
import mimetypes
import bcrypt
from data import queries
from datetime import datetime

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
                messages_archive = queries.get_messages_archive()
                if (len(messages_archive) > 0):
                    session['last_message_id'] = messages_archive[-1]['id']
                    return render_template('chat.html', username = session.get('username'),
                                                        messages = messages_archive)
                else:
                    return render_template('chat.html', username = session.get('username'))                                                        
            else:
                print('Error. Operation forbidden!')
                return render_template('index.html')
        
@app.route("/chat/add_message", methods = ["GET", "POST"])
def add_message():
    message = request.json['messageInputText']
    user = session.get('username')
    date_and_time = datetime.now().strftime('%Y-%m-%d %H:%M')
    print(message, user, date_and_time)
    queries.add_message(message, user, date_and_time)
    data = {'data': message, 'user': user}
    return jsonify(data)

@app.route("/chat/check_messages", methods = ["POST", "GET"])
def check_messages():
    if session.get('last_message_id'):  
        new_messages = queries.get_new_messages(session.get('last_message_id'))
    else:
        new_messages = queries.get_messages_archive()
    if len(new_messages) > 0:
        session['last_message_id'] = new_messages[-1]['id']
        return jsonify(new_messages)
    else:
        return jsonify({'messages': 'NONE'})

if __name__ == '__main__':
    app()
