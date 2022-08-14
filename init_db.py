import sqlite3

conn = sqlite3.connect('database.db')
print ('Opened database successfully')

conn.execute('CREATE TABLE urls (id INTEGER PRIMARY KEY AUTOINCREMENT, longURL TEXT, shortURL TEXT)')
print ('Table created successfully')
conn.close()