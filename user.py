class User:
    def __init__(self, email, name, password, current_status):
        self.email = email
        self.name = name
        self.password = password
        self.curent_status = current_status

    def change_password(self, new_password):
        self.password = new_password
    def change_status(self, new_status):
        self.curent_status = new_status
    #def add_new_skill():

    def get_user_info(self):
        print(f"User {self.name} currently is {self.curent_status}. You can reach them at {self.email}")

