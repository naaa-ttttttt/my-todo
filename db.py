import sqlite3

def init_db():
    connection = sqlite3.connect("todos.db")

    cursor = connection.cursor()

    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            done BOOLEAN DEFAULT 0
        )
    """)

    connection.commit()
    connection.close()


def add_todo(task):
    connection = sqlite3.connect("todos.db")
    cursor = connection.cursor() 
    cursor.execute("INSERT INTO todos (task) VALUES (?)", (task, ))
    connection.commit()
    connection.close()
    print("Ran Successful")


def get_all_todos():
    connection = sqlite3.connect("todos.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM todos")
    rows = cursor.fetchall()
    connection.close()
    return rows

if __name__ == "__main__":
    #add_todo("pray and code")
    print(get_all_todos())
