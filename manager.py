from user import User

class Manager(User):
    def __init__(self, user_id, first_name, last_name, email, city, state, postal_code, phone, user_type):
        super().__init__()
        super().get_user(user_id, first_name, last_name, email, city, state, postal_code, phone, user_type)

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