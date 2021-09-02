import sqlite3
from sqlite3.dbapi2 import connect

with sqlite3.connect('sample.db') as connection:
    c = connection.cursor()
    c.execute('drop table posts')
    c.execute('create table posts(title text, description text)')
    c.execute('insert into posts values("Good", "I\'m good")')
    c.execute('insert into posts values("Well", "I\'m well")')
