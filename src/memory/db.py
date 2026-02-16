import sqlite3

class DatabaseManager:
    """
    DatabaseManager handles connection and queries for the SQLite database.
    """
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = None

    def connect(self):
        """Establishes a connection to the SQLite database."""
        try:
            self.connection = sqlite3.connect(self.db_path)
            print("Database connected successfully.")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def close(self):
        """Closes the database connection."""
        if self.connection:
            self.connection.close()

    # Example query
    def execute_query(self, query, params=None):
        """Execute an SQL query on the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params or ())
            self.connection.commit()
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Database query error: {e}")
            return None

# Usage example:
if __name__ == '__main__':
    db_manager = DatabaseManager("trading_data.db")
    db_manager.connect()
    db_manager.execute_query("CREATE TABLE IF NOT EXISTS trades (id INTEGER PRIMARY KEY, symbol TEXT, quantity REAL)")
    db_manager.close()