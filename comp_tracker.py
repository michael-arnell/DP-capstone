import sqlite3
import datetime
import csv

connection = sqlite3.connect('comp_tracker.db')
cursor = connection.cursor()

class User:
    def __init__(self, first_name, last_name, email, password, city, state, postal_code, phone, user_type):
        self.user_id = None
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.phone = phone
        self.user_type = user_type

    def change_password(self,new_password):
        if new_password:
            self.password = new_password

    def change_first_name(self,new_firstname):
        if new_firstname:
            self.first_name = new_firstname

    def change_last_name(self,new_lastname):
        if new_lastname:
            self.last_name = new_lastname

    def view_competencies(self,query,values):
        pass

    def view_assessments(self,query,values):
        pass

class Manager(User):
    pass

    def add_user(self):
        pass

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

logged_in = False
while logged_in == False:
    print('''\nWelcome to MiCompetency Tracker!\n''')
    username = input('Username: ')
    if username:
        password = input('Password: ')
        if password:
            #query db for username and password
            logged_in = True

print('You are now logged in')