from data import data_manager
from psycopg2 import sql

def add_message(message, user, current_date):
    return data_manager.execute_insert("""
        INSERT INTO messages (message, user_name, submission_date)
        VALUES (%(message)s, %(user)s, %(current_date)s)
    """, {"message": message, "user": user, "current_date": current_date})
