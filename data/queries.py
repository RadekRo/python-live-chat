from data import data_manager
from psycopg2 import sql

def add_message(message, user, current_date):
    return data_manager.execute_insert("""
        INSERT INTO messages (message, user_name, submission_date)
        VALUES (%(message)s, %(user)s, %(current_date)s)
    """, {"message": message, "user": user, "current_date": current_date})

def get_messages_archive():
    return data_manager.execute_select("""
        SELECT id, message, user_name, submission_date
        FROM messages""")

def get_new_messages(last_known_id):
     return data_manager.execute_select("""
        SELECT id, message, user_name, submission_date
        FROM messages
        WHERE id > %(last_known_id)s""", {"last_known_id": last_known_id}, True)