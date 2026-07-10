import sqlite3

def get_connection(db_path="contacts.db"):
    """Return a connection with row_factory set."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def create_table(conn):
    """Create the contacts table if it doesn't exist."""
    conn.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL UNIQUE,
            email TEXT,
            group_name TEXT DEFAULT 'General',
            created_at TEXT DEFAULT (datetime('now'))
        )
    """)
    conn.commit()