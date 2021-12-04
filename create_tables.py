import sqlite3
from manager import Manager

connection = sqlite3.connect('comp_tracker.db')
cursor = connection.cursor()

with open('create_tables.sql') as myfile:
    cursor.executescript(myfile.read())

user = Manager('admin','admin','admin','admin','admin','admin','admin','admin','manager')
user.add_user(cursor,connection)