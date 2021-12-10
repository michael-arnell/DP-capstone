import bcrypt
from getpass import getpass
from os import system, name
from datetime import datetime

class User:
    def __init__(self):
        self.user_id = None
        self.first_name = None
        self.last_name = None
        self.email = None
        self.password = None
        self.city = None
        self.state = None
        self.postal_code = None
        self.phone = None
        self.user_type = None
        self.salt = b'$2b$12$609fYeYkyB5GVhjhcN4ZXu'

    def get_user(self, user_id, first_name, last_name, email, city, state, postal_code, phone, user_type):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        # self.__password = bcrypt.hashpw(password.encode('utf-8'), self.salt)
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.phone = phone
        self.user_type = user_type
    
    def clear(self):
        if name in ('nt','dos'):
            _ = system('cls')
        else:
            _ = system('clear')
    
    def login(self, cursor):
        username = input('Username: ')
        if username:
            password = getpass('Password: ')
        if password:
            values = (username, bcrypt.hashpw(password.encode('utf-8'), self.salt))
            query = 'SELECT user_id, first_name, last_name, email, city, state, postal_code, phone, user_type FROM Users WHERE email = ? and password = ?'
            result = cursor.execute(query,values).fetchone()
            if result:
                user_id, first_name, last_name, email, city, state, postal_code, phone, user_type = result
                self.get_user(user_id, first_name, last_name, email, city, state, postal_code, phone, user_type)
                return True

    def view_user(self, cursor, user_choice = None):
        user_id = user_choice
        if not user_id:
            user_id = input('Please enter the User ID of the user you would like to view: ')
        values = (user_id,)
        query = 'SELECT user_id, first_name, last_name, email, city, state, postal_code, phone, user_type from Users where user_id = ?;'
        user = cursor.execute(query, values).fetchone()
        user_id, first_name, last_name, email, city, state, postal_code, phone, user_type = user
        print(f'''\n1 First Name:  {first_name}
2 Last Name:   {last_name}
3 Email:       {email}
4 City:        {city}
5 State:       {state}
6 Postal Code: {postal_code}
7 Phone:       {phone}
8 User Type:   {user_type}
        ''')
        return {
            '1':'first_name',
            '2':'last_name',
            '3':'email',
            '4':'city',
            '5':'state',
            '6':'postal_code',
            '7':'phone',
            '8':'user_type'
        }

    def change_password(self, new_password, cursor, connection):
        if new_password:
            new_password = bcrypt.hashpw(new_password.encode('utf-8'), self.salt)
            query = 'update Users set password = ? where user_id = ?'
            values = (new_password, self.user_id)
            cursor.execute(query, values)
            connection.commit()
            print('\nYour information has been updated.')
        else:
            print('\nPlease try again.\n')

    def change_first_name(self,new_firstname, cursor, connection):
        if new_firstname:
            self.first_name = new_firstname
            query = 'update Users set first_name = ? where user_id = ?'
            values = (new_firstname, self.user_id)
            cursor.execute(query, values)
            connection.commit()
            self.view_user(cursor, self.user_id)
            print('\nYour information has been updated. See above for reference.')
        else:
            print('\nPlease try again.\n')

    def change_email(self,new_email,cursor,connection):
        if new_email:
            self.email = new_email
            query = 'update Users set email = ? where user_id = ?'
            values = (new_email, self.user_id)
            cursor.execute(query, values)
            connection.commit()
            self.view_user(cursor, self.user_id)
            print('\nYour information has been updated. See above for reference.')
        else:
            print('\nPlease try again.\n')

    def change_last_name(self,new_lastname, cursor, connection):
        if new_lastname:
            self.last_name = new_lastname
            query = 'update Users set last_name = ? where user_id = ?'
            values = (new_lastname, self.user_id)
            cursor.execute(query, values)
            connection.commit()
            self.view_user(cursor, self.user_id)
            print('\nYour information has been updated. See above for reference.')
        else:
            print('\nPlease try again.\n')

    def view_my_competencies(self,cursor):
        query = 'SELECT u.first_name, u.last_name, c.competency_name, ar.score \
                FROM Users u \
                LEFT OUTER JOIN Assessment_Results ar \
                ON u.user_id = ar.user_id \
                INNER JOIN Assessments a \
                ON ar.assessment_id = a.assessment_id \
                INNER JOIN Competencies c \
                ON a.competency_id = c.competency_id \
                WHERE u.user_id = ? \
                ORDER BY ar.date_taken DESC \
                LIMIT 1;'
        values = (self.user_id,)
        rows = cursor.execute(query, values).fetchall()
        print('''\nFirst Name      Last Name       Competency Name       Current Competency Level (0-4)
-------------------------------------------------------------------------------------''')
        for idx in range(len(rows)):
            first_name, last_name, competency_name, score = rows[idx]
            print(f'{first_name:<16}{last_name:<16}{competency_name:<24}{score:^10}')

    def view_my_assessments(self,cursor):
        values = (self.user_id,)
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
