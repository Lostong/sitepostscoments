import sqlite3


def init_db():
    try:
        conn = sqlite3.connect('chat.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS comments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                content TEXT NOT NULL
            )
        ''')
        conn.commit()
        print("База даних створена успішно!")
    except sqlite3.Error as e:
        print(f"Помилка при створенні бази даних: {e}")
    finally:
        conn.close()



def add_comment(username, content):
    conn = sqlite3.connect('chat.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO comments (username, content) VALUES (?, ?)', (username, content))
    conn.commit()
    conn.close()


def get_comments():
    conn = sqlite3.connect('chat.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, username, content FROM comments')
    comments = cursor.fetchall()
    conn.close()
    return comments


def delete_comment(comment_id):
    conn = sqlite3.connect('chat.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM comments WHERE id = ?', (comment_id,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("База даних створена.")

