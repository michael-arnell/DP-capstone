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

menu_choice = None
if current_user.user_type == 'user':
    pass
elif (current_user.user_type) == 'manager':
    while menu_choice != 'E':
        menu_choice = input('''\nPlease select an action to take:

(A)dd a record
(M)odify a record
(V)iew a report
(E)xit application\n''').upper()
        if menu_choice == 'V':
            report_choice = None
            while report_choice != 'B':
                report_choice = input('''\nPlease select the record type you would like to add:

(A)ll users
(C)ompetency
(A)ssessment
(R)esult of assessment
(B)ack to Main Menu\n''').upper()
                if report_choice == 'A':
                    current_user.view_users(cursor)
                elif report_choice == 'S':
                    current_user.view_user(cursor)
        if menu_choice == 'A':
            record_choice = None
            while record_choice != 'B':
                record_choice = input('''\nPlease select the record type you would like to add:

(U)ser
(C)ompetency
(A)ssessment
(R)esult of assessment
(B)ack to Main Menu\n''').upper()
                if record_choice == 'U':
                    current_user.add_user(cursor, connection)
