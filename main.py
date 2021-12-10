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
    while menu_choice != 'E':
        menu_choice = input('''\nPlease select an action to take:

(V)iew my data
(M)odify my personal information
(E)xit application\n''').upper()
        if menu_choice == 'V':
            current_user.clear()
            report_choice = None
            while report_choice != 'B':
                report_choice = input('''\nPlease select the report you would like to view:
            
(1) My Competencies
(2) My Assessment Results
(B)ack to Main Menu\n''').upper()
                if report_choice == '1':
                    current_user.clear()
                    current_user.view_my_competencies(cursor)
                elif report_choice == '2':
                    current_user.clear()
                    current_user.view_my_assessments(cursor)
        if menu_choice == 'M':
            current_user.clear()
            field_choice = None
            while field_choice != 'B':
                field_choice = input('''\nPlease select the field you would like to modify:
            
(F)irst Name
(L)ast Name
(E)mail address
(P)assword
(B)ack to Main Menu\n''').upper()
                if field_choice == 'F':
                    current_user.clear()
                    new_firstname = input('\nPlease enter your updated first name: ')
                    current_user.change_first_name(new_firstname,cursor,connection)
                elif field_choice == 'L':
                    current_user.clear()
                    new_lastname = input('\nPlease enter your updated last name: ')
                    current_user.change_last_name(new_lastname,cursor,connection)
                elif field_choice == 'E':
                    current_user.clear()
                    new_email = input('\nPlease enter your updated email address: ')
                    current_user.change_email(new_email,cursor,connection)
                elif field_choice == 'P':
                    current_user.clear()
                    new_password = input('\nPlease enter your updated password: ')
                    current_user.change_password(new_password,cursor,connection)
elif (current_user.user_type) == 'manager':
    current_user.clear()
    while menu_choice != 'E':
        menu_choice = input('''\nPlease select an action to take:

(A)dd a record
(M)odify  an existing record
(D)elete an assessment result
(I)mport assessment results from csv
(V)iew a report
E(X)port a table
(E)xit application\n''').upper()
        if menu_choice == 'V':
            current_user.clear()
            report_choice = None
            while report_choice != 'B':
                report_choice = input('''\nPlease select the report you would like to view:

(1) All Users
(2) Single User Profile
(3) All Competencies by User
(4) Competency Results Summary
(5) User Competency Summary
(6) User Assessment Results
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
        elif menu_choice == 'X':
                    current_user.clear()
                    report_choice = None
                    while report_choice != 'B':
                        report_choice = input('''\nPlease select the table you would like to export:

        (U)sers
        (C)ompetencies
        (A)ssessments
        (B)ack to Main Menu\n''').upper()
                        if report_choice == 'U':
                            current_user.clear()
                            current_user.export_users_table(cursor)
                        elif report_choice == 'C':
                            current_user.clear()
                            current_user.export_competencies_table(cursor)
                        elif report_choice == 'A':
                            current_user.clear()
                            current_user.export_assessments_table(cursor)