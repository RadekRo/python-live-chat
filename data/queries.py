from data import data_manager
from psycopg2 import sql

def add_message(message, user):
    return data_manager.execute_select("""
        INSERT INTO messages (message, user)
        VALUES (%(message)s, %(user)s)
    """, {"message": message, "user": user}, False)
