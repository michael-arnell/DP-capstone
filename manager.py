from user import User
import bcrypt

class Manager(User):
    def __init__(self, user_id, first_name, last_name, email, city, state, postal_code, phone, user_type):
        super().__init__()
        super().get_user(user_id, first_name, last_name, email, city, state, postal_code, phone, user_type)

    def view_users(self, cursor):
        query = 'SELECT user_id, first_name, last_name, email, city, state, postal_code, phone, user_type from Users;'
        rows = cursor.execute(query).fetchall()
        print('''User ID   First Name  Last Name       Email                City           State  Postal Code  Phone      User Type''')
        for idx in range(len(rows)):
            this_user = list(rows[idx])
            for field in range(len(this_user)):
                if not this_user[field]:
                    this_user[field] = ' '
            user_id, first_name, last_name, email, city, state, postal_code, phone, user_type = this_user
            print(f'{user_id:^10}{first_name:<12}{last_name:<16}{email:<20}{city:<19}{state:<5}{postal_code:<8}{phone:<15}{user_type:<15}')

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

    def add_competency(self):
        pass

    def add_assessment(self):
        pass

    def add_assessment_result(self):
        pass

    def edit_user(self):
        pass

    def edit_competency(self):
        pass

    def edit_assessment(self):
        pass

    def edit_assessment_result(self):
        pass

    def delete_assessment_result(self):
        pass

    def export_csv(self):
        pass

    def import_csv(self):
        pass