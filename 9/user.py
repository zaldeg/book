class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print('User : ', self.first_name.title(), self.last_name.title())

    def greet_user(self):
        print('Hello ', self.first_name.title(), self.last_name.title())
