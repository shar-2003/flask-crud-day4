import sqlite3 as sql

#connect to SQLite
con = sql.connect('books.db')

#Create a Connection
cur = con.cursor()

#Drop books table if already exsist.
cur.execute("DROP TABLE IF EXISTS books")

#Create users table  in db_web database
sql ='''CREATE TABLE "books" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"title"	TEXT,
	"author"	TEXT,
    "published" TEXT
)'''
cur.execute(sql)

#commit changes
con.commit()

#close the connection
con.close()