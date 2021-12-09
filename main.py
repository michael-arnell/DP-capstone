import sqlite3
import csv
from user import *
from manager import *

connection = sqlite3.connect('comp_tracker.db')
cursor = connection.cursor()

current_user = User()
current_user.clear()

logged_in = False
while logged_in != True:
    print('''\nWelcome to MiCompetency Tracker!\n''')
    logged_in = current_user.login(cursor)

if current_user.user_type == 'manager':
    current_user = Manager(current_user.user_id, current_user.first_name, current_user.last_name, current_user.email, current_user.city, current_user.state, current_user.postal_code, current_user.phone, current_user.user_type)

print('\nWelcome ' + current_user.first_name + ' ' + current_user.last_name + '. You are now logged in.')

menu_choice = None
if current_user.user_type == 'user':
    current_user.clear()
elif (current_user.user_type) == 'manager':
    current_user.clear()
    while menu_choice != 'E':
        menu_choice = input('''\nPlease select an action to take:

(A)dd a record
(M)odify or delete an existing record
(D)elete an assessment result
(I)mport assessment results from csv
(V)iew a report
(E)xit application\n''').upper()
        if menu_choice == 'V':
            current_user.clear()
            report_choice = None
            while report_choice != 'B':
                report_choice = input('''\nPlease select the report you would like to view:

(1) All users
(2) Single user profile
(3) All competencies by user
(4) Single competency for all users
(5) All competencies for a single user
(6) All assessment results for a single user
(B)ack to Main Menu\n''').upper()
                if report_choice == '1':
                    current_user.clear()
                    current_user.view_users(cursor)
                elif report_choice == '2':
                    current_user.clear()
                    current_user.view_user(cursor)
                elif report_choice == '3':
                    current_user.clear()
                    current_user.view_competencies_by_user(cursor)
                elif report_choice == '4':
                    current_user.clear()
                    current_user.view_single_competency(cursor)
                elif report_choice == '5':
                    current_user.clear()
                    current_user.view_single_user_competencies(cursor)
                elif report_choice == '6':
                    current_user.clear()
                    current_user.view_single_user_assessments(cursor)
        elif menu_choice == 'A':
            current_user.clear()
            record_choice = None
            while record_choice != 'B':
                record_choice = input('''\nPlease select the record type you would like to add:

(U)ser
(C)ompetency
(A)ssessment
(R)esult of assessment
(B)ack to Main Menu\n''').upper()
                if record_choice == 'U':
                    current_user.clear()
                    current_user.add_user(cursor, connection)
                elif record_choice == 'C':
                    current_user.clear()
                    current_user.add_competency(cursor,connection)
                elif record_choice == 'A':
                    current_user.clear()
                    current_user.add_assessment(cursor,connection)
                elif record_choice == 'R':
                    current_user.clear()
                    current_user.add_assessment_result(cursor,connection)
        elif menu_choice == 'I':
            current_user.clear()
            current_user.import_results(cursor,connection)
        elif menu_choice == 'M':
            current_user.clear()
            record_type = None
            while record_type != 'B':
                record_type = input('''\nPlease select the record type you would like to modify:

(U)ser
(C)ompetency
(A)ssessment
(R)esults of an assessment
(B)ack to Main Menu\n''').upper()
                if record_type == 'U':
                    current_user.clear()
                    current_user.edit_user(cursor,connection)
                elif record_type == 'C':
                    current_user.clear()
                    current_user.edit_competency(cursor,connection)
                elif record_type == 'A':
                    current_user.clear()
                    current_user.edit_assessment(cursor,connection)
                elif record_type == 'R':
                    current_user.clear()
                    current_user.edit_assessment_result(cursor,connection)
        elif menu_choice == 'D':
            current_user.clear()
            current_user.delete_assessment_result(cursor,connection)
