import sqlite3
import time
import sys

DB_PATH = 'database.db'

def get_columns(cursor, table):
    cursor.execute(f"PRAGMA table_info('{table}')")
    return [row[1] for row in cursor.fetchall()]

def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Check if table exists
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='FAVORIETEN'")
    if not cur.fetchone():
        print('No FAVORIETEN table found — creating correct table.')
        cur.execute("""CREATE TABLE IF NOT EXISTS FAVORIETEN (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            dier_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES USERS(id),
            FOREIGN KEY (dier_id) REFERENCES DIEREN(id),
            UNIQUE(user_id, dier_id)
        )""")
        conn.commit()
        conn.close()
        print('Created FAVORIETEN table.')
        return

    cols = get_columns(cur, 'FAVORIETEN')
    expected = ['id', 'user_id', 'dier_id']
    if cols == expected:
        print('FAVORIETEN table already has the expected schema.')
        conn.close()
        return

    # Schema mismatch — rename old table and create new one
    timestamp = int(time.time())
    backup_name = f'FAVORIETEN_OLD_{timestamp}'
    print(f"Schema mismatch for FAVORIETEN (columns: {cols}). Renaming to {backup_name} and creating new table.")
    try:
        cur.execute(f"ALTER TABLE FAVORIETEN RENAME TO {backup_name}")
    except sqlite3.OperationalError as e:
        print('Failed to rename table:', e)
        conn.close()
        sys.exit(1)

    cur.execute("""CREATE TABLE FAVORIETEN (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        dier_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES USERS(id),
        FOREIGN KEY (dier_id) REFERENCES DIEREN(id),
        UNIQUE(user_id, dier_id)
    )""")

    conn.commit()
    conn.close()
    print('Migration complete. Old table preserved as', backup_name)

if __name__ == '__main__':
    main()
