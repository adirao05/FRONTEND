import sqlite3
import bcrypt

# Connect to SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect('db/users.db')
cursor = conn.cursor()

# Create table for users
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
)
''')
conn.commit()

# Add a sample user (hashed password)
def add_user(username, password):
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed))
    conn.commit()

# Example: Adding a test user (replace with actual signup logic)
add_user('testuser', 'test123')

conn.close()
print("Database created successfully.")
