import bcrypt
from getpass import getpass
from os import system, name

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

    def change_password(self, new_password, cursor, connection):
        if new_password:
            new_password = bcrypt.hashpw(new_password.encode('utf-8'), self.salt)
            print(new_password)
            query = 'update Users set password = ? where user_id = ?'
            values = (new_password, self.user_id)
            cursor.execute(query, values)
            connection.commit()

    def change_first_name(self,new_firstname):
        if new_firstname:
            self.first_name = new_firstname

    def change_last_name(self,new_lastname):
        if new_lastname:
            self.last_name = new_lastname

    def view_competencies(self,query,values):
        query = 'SELECT c.competency_name, AVG(ar.score) \
                FROM Users u \
                INNER JOIN Assessment_Results ar ON u.user_id = ar.user_id \
                INNER JOIN Assessments a on ar.assessment_id = a.assessment_id \
                INNER JOIN Competencies c on a.competency_id = c.competency_id \
                WHERE u.user_id = ?'
        values = (self.user_id)

    def view_assessments(self,query,values):
        pass