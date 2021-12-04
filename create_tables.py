import sqlite3

connection = sqlite3.connect('comp_tracker.db')
cursor = connection.cursor()

with open('create_tables.sql') as myfile:
    cursor.executescript(myfile.read())