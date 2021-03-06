from user import User
import bcrypt
from datetime import datetime
import csv
from os import system, name

class Manager(User):
    def __init__(self, user_id, first_name, last_name, email, city, state, postal_code, phone, user_type):
        super().__init__()
        super().get_user(user_id, first_name, last_name, email, city, state, postal_code, phone, user_type)

    def view_users(self, cursor):
        query = 'SELECT user_id, first_name, last_name, email, city, state, postal_code, phone, user_type from Users;'
        rows = cursor.execute(query).fetchall()
        print('''User ID   First Name  Last Name       Email               City              State  Postal Code  Phone       User Type
---------------------------------------------------------------------------------------------------------------------''')
        for idx in range(len(rows)):
            this_user = list(rows[idx])
            for field in range(len(this_user)):
                if not this_user[field]:
                    this_user[field] = ' '
            user_id, first_name, last_name, email, city, state, postal_code, phone, user_type = this_user
            print(f'{user_id:^10}{first_name:<12}{last_name:<16}{email:<20}{city:<18}{state:<7}{postal_code:<13}{phone:<12}{user_type:<15}')

    def view_competencies_by_user(self, cursor):
        query = 'SELECT first_name, last_name, competency_name, score \
                FROM (SELECT u.user_id, u.first_name, u.last_name, c.competency_id, c.competency_name, ar.score, ar.date_taken \
                FROM Users u \
                LEFT OUTER JOIN Assessment_Results ar \
                ON u.user_id = ar.user_id \
                INNER JOIN Assessments a \
                ON ar.assessment_id = a.assessment_id \
                INNER JOIN Competencies c \
                ON a.competency_id = c.competency_id \
                ORDER BY ar.date_taken DESC) AS x \
                GROUP BY user_id, competency_id;'
        rows = cursor.execute(query).fetchall()
        print('''\nFirst Name      Last Name       Competency Name       Current Competency Level (0-4)
-------------------------------------------------------------------------------------''')
        for idx in range(len(rows)):
            first_name, last_name, competency_name, score = rows[idx]
            print(f'{first_name:<16}{last_name:<16}{competency_name:<24}{score:^10}')

    def view_single_competency(self, cursor):
        self.view_all_competencies(cursor)
        try:
            values = (int(input('\nPlease enter the ID of the competency you would like to review: ')),)
            query = 'SELECT competency_name FROM Competencies WHERE competency_id = ?'
            competency_name = cursor.execute(query,values).fetchone()[0]
            query = 'SELECT AVG(score) FROM (SELECT first_name, last_name, competency_name, score \
                    FROM (SELECT u.user_id, u.first_name, u.last_name, c.competency_id, c.competency_name, ar.score, ar.date_taken \
                    FROM Users u \
                    LEFT OUTER JOIN Assessment_Results ar \
                    ON u.user_id = ar.user_id \
                    INNER JOIN Assessments a \
                    ON ar.assessment_id = a.assessment_id \
                    INNER JOIN Competencies c \
                    ON a.competency_id = c.competency_id \
                    WHERE a.competency_id = ? \
                    ORDER BY ar.date_taken DESC) AS x \
                    GROUP BY user_id, competency_id) as y;'
            average = cursor.execute(query,values).fetchone()[0]
            print(f"\nThe average competency for all users in '{competency_name}' is {average}.\n")
            query = 'SELECT first_name, last_name, competency_name, score \
                    FROM (SELECT u.user_id, u.first_name, u.last_name, c.competency_id, c.competency_name, ar.score, ar.date_taken \
                    FROM Users u \
                    LEFT OUTER JOIN Assessment_Results ar \
                    ON u.user_id = ar.user_id \
                    INNER JOIN Assessments a \
                    ON ar.assessment_id = a.assessment_id \
                    INNER JOIN Competencies c \
                    ON a.competency_id = c.competency_id \
                    WHERE a.competency_id = ? \
                    ORDER BY ar.date_taken DESC) AS x \
                    GROUP BY user_id, competency_id;'
            rows = cursor.execute(query,values).fetchall()
            print('''\nFirst Name      Last Name       Competency Name       Current Competency Level (0-4)
-------------------------------------------------------------------------------------''')
            for idx in range(len(rows)):
                first_name, last_name, competency_name, score = rows[idx]
                print(f'{first_name:<16}{last_name:<16}{competency_name:<24}{score:^10}')
        except:
            print('\nAn error has occurred. Please try again.\n')

    def view_single_user_competencies(self, cursor):
        self.view_users(cursor)
        try:
            values = (int(input('\nPlease enter the ID of the user you would like to review: ')),)
            query = 'SELECT first_name, last_name FROM Users WHERE user_id = ?'
            user_name = cursor.execute(query,values).fetchone()
            full_name = user_name[0] + ' ' + user_name[1]
            query = 'SELECT AVG(score) FROM (SELECT first_name, last_name, email, competency_name, score \
                    FROM (SELECT u.user_id, u.first_name, u.last_name, u.email, c.competency_id, c.competency_name, ar.score, ar.date_taken \
                    FROM Users u \
                    LEFT OUTER JOIN Assessment_Results ar \
                    ON u.user_id = ar.user_id \
                    INNER JOIN Assessments a \
                    ON ar.assessment_id = a.assessment_id \
                    INNER JOIN Competencies c \
                    ON a.competency_id = c.competency_id \
                    WHERE u.user_id = ? \
                    ORDER BY ar.date_taken DESC) AS x \
                    GROUP BY user_id, competency_id) as y;'
            average = cursor.execute(query,values).fetchone()[0]
            print(f"\nThe average competency for {full_name} across all competencies is {average}.\n")
            query = 'SELECT first_name, last_name, email, competency_name, score \
                    FROM (SELECT u.user_id, u.first_name, u.email, u.last_name, c.competency_id, c.competency_name, ar.score, ar.date_taken \
                    FROM Users u \
                    LEFT OUTER JOIN Assessment_Results ar \
                    ON u.user_id = ar.user_id \
                    INNER JOIN Assessments a \
                    ON ar.assessment_id = a.assessment_id \
                    INNER JOIN Competencies c \
                    ON a.competency_id = c.competency_id \
                    WHERE u.user_id = ? \
                    ORDER BY ar.date_taken DESC) AS x \
                    GROUP BY user_id, competency_id;'
            rows = cursor.execute(query,values).fetchall()
            print('''\nFirst Name      Last Name       Email               Competency Name       Current Competency Level (0-4)
----------------------------------------------------------------------------------------------------''')
            for idx in range(len(rows)):
                first_name, last_name, email, competency_name, score = rows[idx]
                print(f'{first_name:<16}{last_name:<16}{email:<20}{competency_name:<24}{score:^10}')
        except:
            print('\nAn error has occurred. Please try again.\n')

    def view_single_user_assessments(self, cursor, user_choice = None):
        try:
            user_id = user_choice
            if not user_id:
                self.view_users(cursor)
                values = (int(input('\nPlease enter the ID of the user you would like to review: ')),)
            else:
                values = (user_id,)
            query = 'SELECT u.first_name, u.last_name, c.competency_name, a.assessment_id, a.assessment_name, ar.score, ar.date_taken \
                    FROM Users u \
                    LEFT OUTER JOIN Assessment_Results ar \
                    ON u.user_id = ar.user_id \
                    INNER JOIN Assessments a \
                    ON ar.assessment_id = a.assessment_id \
                    INNER JOIN Competencies c \
                    ON a.competency_id = c.competency_id \
                    WHERE u.user_id = ? \
                    ORDER BY ar.date_taken ASC;'
            rows = cursor.execute(query,values).fetchall()
            print('''\nResult ID First Name      Last Name       Competency Name         Assessment Name        Score    Date Taken
-----------------------------------------------------------------------------------------------------------''')
            for idx in range(len(rows)):
                first_name, last_name, competency_name, assessment_id, assessment_name, score, date_taken = rows[idx]
                print(f'{idx + 1:^10}{first_name:<16}{last_name:<16}{competency_name:<24}{assessment_name:<20}{score:^12}{datetime.strftime(datetime.fromtimestamp(date_taken),"%Y-%m-%d"):<15}')
            return rows
        except:
            print('\nAn error has occurred. Please try again.\n')

    def add_user(self, cursor, connection):
        try:
            query = 'INSERT into Users (first_name, last_name, email, password, city, state, postal_code, phone, user_type) \
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);'
            first_name = input('\nFirst Name (required): ')
            last_name = input('Last Name (required): ')
            email = input('Email (required): ')
            password = bcrypt.hashpw(input('Password (required): ').encode('utf-8'),self.salt)
            city = input('City: ')
            state = input('State: ')
            postal_code = input('Postal Code: ')
            phone = input('Phone: ')
            user_choice = None
            while user_choice not in ['U','M']:
                user_choice = input('User Type - Please select (U)ser or (M)anager (required): ').upper()
            if user_choice == 'U':
                user_type = 'user'
            else:
                user_type = 'manager'
            values = (first_name, last_name, email, password, city, state, postal_code, phone, user_type)
            cursor.execute(query,values)
            connection.commit()
            self.view_users(cursor)
            print('\nYour new user record has been successfully added. See above for reference.')
        except:
            print('\nAn error has occurred. Please try again.\n')

    def add_competency(self, cursor, connection):
        query = 'INSERT into Competencies (competency_name, date_created) \
                VALUES (?, ?);'
        competency_name = input('\nCompetency Name: ')
        try:
            date_created = int(datetime.today().timestamp())
            values = (competency_name, date_created)
            cursor.execute(query,values)
            connection.commit()
            self.view_all_competencies(cursor)
            print('\nYour competency record has been successfully added. See above for reference.')
        except:
            print('\nAn error has occurred. Please try again.\n')

    def add_assessment(self, cursor, connection):
        self.view_all_competencies(cursor)
        try:
            competency_id = int(input('\nPlease enter the ID of the competency tested by this assessment: '))
            query = 'INSERT into Assessments (assessment_name, competency_id) \
                    VALUES (?, ?);'
            assessment_name = input('\nPlease enter the Assessment Name: ')
            values = (assessment_name, competency_id)
            cursor.execute(query,values)
            connection.commit()
            self.view_all_assessments(cursor)
            print('\nYour assessment has been successfully added. See above for reference.')
        except:
            print('\nAn error has occurred. Please try again.\n')

    def add_assessment_result(self, cursor, connection):
        try:
            self.view_users(cursor)
            user_id = int(input('\nPlease enter the ID of the user that completed the assessment: '))
            self.view_all_assessments(cursor)
            assessment_id = int(input('\nPlease enter the ID of the assessment completed: '))
            score = int(input('\nPlease enter the score received (0 - 4): '))
            date_taken = int(datetime.strptime(input('\nPlease enter the date the assessment was completed in the format YYYY-mm-dd: '),'%Y-%m-%d').timestamp())
            manager = input('Would you like to include the manager who administered the assessment? (Y) or (N): ').upper()
            if manager == 'Y':
                self.view_users(cursor)
                manager_id = int(input('\nPlease enter the ID of the manager that administered the assessment: '))
                values = (user_id, assessment_id, score, date_taken, manager_id)
                query = 'INSERT into Assessment_Results (user_id, assessment_id, score, date_taken, manager_id) \
                    VALUES (?, ?, ?, ?, ?);'
            else:
                values = (user_id, assessment_id, score, date_taken)
                query = 'INSERT into Assessment_Results (user_id, assessment_id, score, date_taken) \
                    VALUES (?, ?, ?, ?);'
            cursor.execute(query,values)
            connection.commit()
            self.view_single_user_assessments(cursor,user_id)
            print('\nYour assessment result has been successfully added. See above for reference.')
        except:
            print('\nAn error has occurred. Please try again.\n')

    def edit_user(self, cursor, connection):
        try:
            self.view_users(cursor)
            user_id = int(input('\nPlease enter the ID of the user you would like to modify: '))
            fields = self.view_user(cursor, user_id)
            field = fields[input('\nPlease enter the number of the field you would like to modify: ')]
            new_value = input(f'\nPlease enter the new value of this field: ')
            values = (new_value, user_id)
            query = 'UPDATE Users SET ' + field + ' = ? WHERE user_id = ?;'
            cursor.execute(query,values)
            connection.commit()
            self.view_users(cursor)
            print('\nYour new user record has been successfully modified. See above for reference.')
        except:
            print('\nAn error has occurred. Please try again.\n')

    def edit_competency(self, cursor, connection):
        try:
            self.view_all_competencies(cursor)
            competency_id = int(input('\nPlease enter the ID of the competency you would like to modify: '))
            competency_name = input('\nPlease enter your updated competency name: ')
            values = (competency_name, competency_id)
            query = 'UPDATE Competencies SET competency_name = ? WHERE competency_id = ?;'
            cursor.execute(query,values)
            connection.commit()
            self.view_all_competencies(cursor)
            print('\nYour competency record has been successfully modified. See above for reference.')
        except:
            print('\nAn error has occurred. Please try again.\n')

    def edit_assessment(self, cursor, connection):
        try:
            self.view_all_assessments(cursor)
            assessment_id = int(input('\nPlease enter the ID of the assessment you would like to modify: '))
            assessment_name = input('\nPlease enter your updated competency name: ')
            values = (assessment_name, assessment_id)
            query = 'UPDATE Assessments SET assessment_name = ? WHERE assessment_id = ?;'
            cursor.execute(query,values)
            connection.commit()
            self.view_all_assessments(cursor)
            print('\nYour assessment has been successfully modified. See above for reference.')
        except:
            print('\nAn error has occurred. Please try again.\n')

    def edit_assessment_result(self, cursor, connection):
        try:
            self.view_users(cursor)
            user_id = int(input('\nPlease enter the ID of the user whose results you would like to modify: '))
            self.clear()
            results = self.view_single_user_assessments(cursor, user_id)
            result_id = int(input('\nPlease enter the ID of the result you would like to modify: '))
            new_score = int(input('\nPlease enter the updated score for this assessment result: '))
            values = (new_score, results[result_id - 1][3],user_id)
            query = 'UPDATE Assessment_Results SET score = ? WHERE assessment_id = ? AND user_id = ?;'
            cursor.execute(query,values)
            connection.commit()
            self.view_single_user_assessments(cursor, user_id)
            print('\nYour assessment result has been successfully modified. See above for reference.')
        except:
            print('\nAn error has occurred. Please try again.\n')

    def delete_assessment_result(self, cursor, connection):
        try:
            self.view_users(cursor)
            user_id = int(input('\nPlease enter the ID of the user whose results you would like to delete: '))
            self.clear()
            results = self.view_single_user_assessments(cursor, user_id)
            result_id = int(input('\nPlease enter the ID of the result you would like to delete: '))
            values = (results[result_id - 1][3],user_id)
            query = 'DELETE FROM Assessment_Results WHERE assessment_id = ? AND user_id = ?;'
            cursor.execute(query,values)
            connection.commit()
            self.view_single_user_assessments(cursor, user_id)
            print('\nYour assessment result has been successfully deleted. See above for reference.')
        except:
            print('\nAn error has occurred. Please try again.\n')

    def export_users_table(self,cursor):
        query = 'SELECT user_id, first_name, last_name, email, city, state, postal_code, phone, user_type from Users;'
        rows = cursor.execute(query).fetchall()
        with open('users.csv', 'w') as report_file:
            fields = ['User ID','First Name','Last Name','Email','City','State','Postal Code','Phone','User Type']
            writer = csv.writer(report_file)
            writer.writerow(fields)
            writer.writerows(rows)

    def export_competencies_table(self,cursor):
        query = 'SELECT * FROM Competencies;'
        rows = cursor.execute(query).fetchall()
        new_rows = []
        for row in rows:
            row = list(row)
            row[2] = datetime.strftime(datetime.fromtimestamp(row[2]),'%Y-%m-%d')
            new_rows.append(row)
        with open('competencies.csv', 'w') as report_file:
            fields = ['Competency ID','Competency Name','Date Created']
            writer = csv.writer(report_file)
            writer.writerow(fields)
            writer.writerows(new_rows)

    def export_assessments_table(self,cursor):
        query = 'SELECT a.assessment_id, a.assessment_name, c.competency_id, c.competency_name FROM Assessments a \
                INNER JOIN Competencies c ON a.competency_id = c.competency_id;'
        rows = cursor.execute(query).fetchall()
        with open('assessments.csv', 'w') as report_file:
            fields = ['Assessment ID','Assessment Name','Competency ID','Competency Name']
            writer = csv.writer(report_file)
            writer.writerow(fields)
            writer.writerows(rows)

    def import_results(self, cursor, connection):
        try:
            filename = input('\nPlease enter the name of the CSV file you would like to import (without the file extension): ')
            with open(filename + '.csv', 'r') as importfile:
                results = list(csv.DictReader(importfile))
            for idx in range(len(results)):
                query = 'INSERT INTO Assessment_Results (user_id, assessment_id, score, date_taken, manager_id) \
                        VALUES (?,?,?,?,?)'
                values = (results[idx]['User ID'], results[idx]['Assessment ID'], results[idx]['Score'], int(datetime.strptime(results[idx]['Date Taken'],'%Y-%m-%d').timestamp()), results[idx]['Manager ID'])
                cursor.execute(query,values)
            connection.commit()
            print('\nYour file has been successfully imported.')
        except:
            print('\nAn error has occurred. Please try again.\n')
            
    def view_all_competencies(self, cursor):
        query = 'SELECT * FROM Competencies;'
        rows = cursor.execute(query).fetchall()
        print('''\nCompetency ID   Competency Name               Date Created
----------------------------------------------------------''')
        for idx in range(len(rows)):
            competency_id, competency_name, date_created = rows[idx]
            print(f'{competency_id:^16}{competency_name:<30}{datetime.strftime(datetime.fromtimestamp(date_created),"%Y-%m-%d"):<10}')

    def view_all_assessments(self, cursor):
        query = 'SELECT a.assessment_id, a.assessment_name, c.competency_name FROM Assessments a \
                INNER JOIN Competencies c ON a.competency_id = c.competency_id;'
        rows = cursor.execute(query).fetchall()
        print('''\nAssessment ID   Assessment Name   Competency Name
-----------------------------------------------''')
        for idx in range(len(rows)):
            assessment_id, assessment_name, competency_name = rows[idx]
            print(f'{assessment_id:^16}{assessment_name:<18}{competency_name:<10}')
