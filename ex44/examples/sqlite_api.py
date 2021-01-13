# Following along with the `sqlite3 - DB-API 2.0
# interface for SQLite databases` docs
# found here:  https://docs.python.org/3.10/library/sqlite3.html
import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY','RHAT', 100, 35.14)")

# Save (commit) the changes
conn.commit()

# We can allso close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
