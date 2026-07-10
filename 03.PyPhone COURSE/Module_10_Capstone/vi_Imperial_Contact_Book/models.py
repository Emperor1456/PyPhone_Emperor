from database import get_connection, create_table

def add_contact(name, phone, email=None, group_name="General"):
    """Insert a new contact. Returns True on success."""
    with get_connection() as conn:
        create_table(conn)
        conn.execute(
            "INSERT INTO contacts (name, phone, email, group_name) VALUES (?, ?, ?, ?)",
            (name, phone, email, group_name)
        )
        conn.commit()
    return True

def list_contacts():
    """Return all contacts as a list of dicts."""
    with get_connection() as conn:
        create_table(conn)
        rows = conn.execute("SELECT * FROM contacts ORDER BY name").fetchall()
        return [dict(row) for row in rows]

def search_contacts(query):
    """Return contacts where name or group contains query."""
    with get_connection() as conn:
        create_table(conn)
        rows = conn.execute(
            "SELECT * FROM contacts WHERE name LIKE ? OR group_name LIKE ?",
            (f"%{query}%", f"%{query}%")
        ).fetchall()
        return [dict(row) for row in rows]

def update_phone(contact_id, new_phone):
    """Update the phone number of a contact. Returns True if a row was updated."""
    with get_connection() as conn:
        create_table(conn)
        cursor = conn.execute(
            "UPDATE contacts SET phone = ? WHERE id = ?",
            (new_phone, contact_id)
        )
        conn.commit()
        return cursor.rowcount > 0

def delete_contact(contact_id):
    """Delete a contact by id. Returns True if a row was deleted."""
    with get_connection() as conn:
        create_table(conn)
        cursor = conn.execute(
            "DELETE FROM contacts WHERE id = ?",
            (contact_id,)
        )
        conn.commit()
        return cursor.rowcount > 0