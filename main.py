import sqlite3
import datetime
import csv
import bcrypt
from user import *
from manager import *
from getpass import getpass

connection = sqlite3.connect('comp_tracker.db')
cursor = connection.cursor()

current_user = User()

logged_in = False
while logged_in != True:
    print('''\nWelcome to MiCompetency Tracker!\n''')
    logged_in = current_user.login(cursor)

if current_user.user_type == 'manager':
    current_user = Manager(current_user.user_id, current_user.first_name, current_user.last_name, current_user.email, current_user.city, current_user.state, current_user.postal_code, current_user.phone, current_user.user_type)

print('\nWelcome ' + current_user.first_name + ' ' + current_user.last_name + '. You are now logged in.')
