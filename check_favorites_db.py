import sqlite3

DB='database.db'
conn=sqlite3.connect(DB)
cur=conn.cursor()
cur.execute("PRAGMA table_info('FAVORIETEN')")
cols=cur.fetchall()
print('columns:', [c[1] for c in cols])
cur.execute('SELECT count(*) FROM FAVORIETEN')
print('rows:', cur.fetchone()[0])
conn.close()
