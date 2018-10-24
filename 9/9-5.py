class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print('User : ', self.first_name.title(), self.last_name.title())

    def greet_user(self):
        print('Hello ', self.first_name.title(), self.last_name.title())

    def increment_login_attempt(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User('aleksey', 'zaitcev')
user.describe_user()
user.greet_user()
user.increment_login_attempt()
user.increment_login_attempt()
user.increment_login_attempt()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)
