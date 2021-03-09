import sqlite3

db = sqlite3.connect('test_base.sqlite')
cursor = db.cursor()

cursor.execute('CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)')

cursor.execute('INSERT INTO books VALUES(1, "Selfish Gene", "Richard Dawkins", "8.5")')
db.commit()

cursor.close()
