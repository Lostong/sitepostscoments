import sqlite3

def init():
    connection = sqlite3.connect("database.db")
    create_table = '''CREATE TABLE IF NOT EXISTS comments (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      text TEXT NOT NULL,
                      description TEXT NOT NULL);'''
    cursor = connection.cursor()
    cursor.execute(create_table)
    connection.commit()
    connection.close()

init()
def get_db_connection():
  connection = sqlite3.connect("database.db", timeout=10) # timeout - закрывает бд если ее не использовали сам через время
  connection.row_factory = sqlite3.Row
  return connection


def get_comments(comments_id):
  connection = get_db_connection()
  select_query = "SELECT * FROM comments WHERE id=?"
  comments = connection.execute(select_query, (comments_id,)).fetchone()
  connection.close()
  return comments


def create(text, description):
    connection = get_db_connection()
    create_query = "INSERT INTO comments (text, description) VALUES (?, ?)"
    index = connection.execute(create_query, (text, description)).lastrowid
    connection.commit()
    connection.close()
    return index


def update(comments_id, text, description):
   connection = get_db_connection()
   connection.execute("UPDATE comments SET name=?, ingredients=?, price=? WHERE id=?",
                      (text, description, comments_id))
   connection.commit()
   connection.close()
   return 202


def delete(comments_id):
   connection = get_db_connection()
   connection.execute('DELETE FROM comments WHERE id = ?', (comments_id,))
   connection.commit()
   connection.close()
   return 200


def get_all_comments():
    connection = get_db_connection()
    select_query = "SELECT * FROM comments"
    commentss = connection.execute(select_query).fetchall()
    connection.close()
    return commentss

def limit():
    connection = get_db_connection()
    limit_query = "SELECT COUNT(*) FROM comments"
    limit_number = connection.execute(limit_query).fetchone()[0]
    connection.close()
    return int(limit_number)