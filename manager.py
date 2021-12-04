from user import User
import bcrypt
from datetime import datetime

class Manager(User):
    def __init__(self, user_id, first_name, last_name, email, city, state, postal_code, phone, user_type):
        super().__init__()
        super().get_user(user_id, first_name, last_name, email, city, state, postal_code, phone, user_type)

    def view_users(self, cursor):
        query = 'SELECT user_id, first_name, last_name, email, city, state, postal_code, phone, user_type from Users;'
        rows = cursor.execute(query).fetchall()
        print('''User ID   First Name  Last Name       Email               City              State  Postal Code  Phone       User Type''')
        for idx in range(len(rows)):
            this_user = list(rows[idx])
            for field in range(len(this_user)):
                if not this_user[field]:
                    this_user[field] = ' '
            user_id, first_name, last_name, email, city, state, postal_code, phone, user_type = this_user
            print(f'{user_id:^10}{first_name:<12}{last_name:<16}{email:<20}{city:<18}{state:<7}{postal_code:<13}{phone:<12}{user_type:<15}')

    def view_user(self, cursor):
        email = input('Please enter the email of the user you would like to view: ')
        values = (email,)
        query = 'SELECT user_id, first_name, last_name, email, city, state, postal_code, phone, user_type from Users where email = ?;'
        user = cursor.execute(query, values).fetchone()
        user_id, first_name, last_name, email, city, state, postal_code, phone, user_type = user
        print(f'''\nUser ID: {user_id}
First Name:  {first_name}
Last Name:   {last_name}
Email:       {email}
City:        {city}
State:       {state}
Postal Code: {postal_code}
Phone:       {phone}
User Type:   {user_type}
        ''')

    def view_competencies_by_user(self, cursor):
        pass

    def view_single_competency(self, cursor):
        pass

    def view_single_user_competencies(self, cursor):
        pass

    def view_single_user_assessments(self, cursor):
        pass

    def add_user(self, cursor, connection):
        query = 'INSERT into Users (first_name, last_name, email, password, city, state, postal_code, phone, user_type) \
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);'
        first_name = input('\nFirst Name: ')
        last_name = input('Last Name: ')
        email = input('Email: ')
        password = bcrypt.hashpw(input('Password: ').encode('utf-8'),self.salt)
        city = input('City: ')
        state = input('State: ')
        postal_code = input('Postal Code: ')
        phone = input('Phone: ')
        user_choice = None
        while user_choice not in ['U','M']:
            user_choice = input('User Type - Please select (U)ser or (M)anager: ').upper()
        if user_choice == 'U':
            user_type = 'user'
        else:
            user_type = 'manager'
        values = (first_name, last_name, email, password, city, state, postal_code, phone, user_type)
        cursor.execute(query,values)
        connection.commit()

    def add_competency(self, cursor, connection):
        query = 'INSERT into Competencies (competency_name, date_created) \
                VALUES (?, ?);'
        competency_name = input('\nCompetency Name: ')
        date_created = datetime.today().strftime('%Y-%m-%d')
        values = (competency_name, date_created)
        cursor.execute(query,values)
        connection.commit()
        print('\nYour competency record has been successfully added.')

    def add_assessment(self, cursor, connection):
        self.view_all_competencies(cursor)
        competency_id = int(input('\nPlease enter the ID of the competency tested by this assessment: '))
        query = 'INSERT into Assessments (assessment_name, competency_id) \
                VALUES (?, ?);'
        assessment_name = input('\nPlease enter the Assessment Name: ')
        values = (assessment_name, competency_id)
        cursor.execute(query,values)
        connection.commit()
        print('\nYour assessment has been successfully added.')

    def add_assessment_result(self, cursor, connection):
        self.view_users(cursor)
        user_id = int(input('\nPlease enter the ID of the user that completed the assessment: '))
        self.view_all_assessments(cursor)
        assessment_id = int(input('\nPlease enter the ID of the assessment completed: '))
        score = int(input('\nPlease enter the score received (0 - 4): '))
        date_taken = input('\nPlease enter the date the assessment was completed: ')
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
        print('\nYour assessment result has been successfully added.')


    def edit_user(self, cursor, connection):
        pass

    def edit_competency(self, cursor, connection):
        pass

    def edit_assessment(self, cursor, connection):
        pass

    def edit_assessment_result(self, cursor, connection):
        pass

    def delete_assessment_result(self, cursor, connection):
        pass

    def export_csv(self):
        pass

    def import_csv(self):
        pass

    def view_all_competencies(self, cursor):
        query = 'SELECT * FROM Competencies;'
        rows = cursor.execute(query).fetchall()
        print('''\nCompetency ID   Competency Name   Date Created''')
        for idx in range(len(rows)):
            competency_id, competency_name, date_created = rows[idx]
            print(f'{competency_id:^16}{competency_name:<18}{date_created:<10}')

    def view_all_assessments(self, cursor):
        query = 'SELECT a.assessment_id, a.assessment_name, c.competency_name FROM Assessments a \
                INNER JOIN Competencies c ON a.competency_id = c.competency_id;'
        rows = cursor.execute(query).fetchall()
        print('''\nAssessment ID   Assessment Name   Competency Name''')
        for idx in range(len(rows)):
            assessment_id, assessment_name, competency_name = rows[idx]
            print(f'{assessment_id:^16}{assessment_name:<18}{competency_name:<10}')
