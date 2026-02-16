import sqlite3

# Initialize SQLite database
conn = sqlite3.connect('trade_memory.db')
cursor = conn.cursor()

# Create signals table
cursor.execute('''
CREATE TABLE IF NOT EXISTS signals (
    id INTEGER PRIMARY KEY,
    timestamp DATETIME,
    ...
)
''')

# Create trades table
cursor.execute('''
CREATE TABLE IF NOT EXISTS trades (
    id INTEGER PRIMARY KEY,
    timestamp DATETIME,
    ...
)
''')

# Create decisions table
cursor.execute('''
CREATE TABLE IF NOT EXISTS decisions (
    id INTEGER PRIMARY KEY,
    timestamp DATETIME,
    ...
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()