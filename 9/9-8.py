class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print('User : ', self.first_name.title(), self.last_name.title())

    def greet_user(self):
        print('Hello ', self.first_name.title(), self.last_name.title())


class Priveleges:
    def __init__(self):
        self.privileges = ['разрешено добавлять сообщение', 'разрешено удалять сообщения',
                           'разрешено банить пользователей']

    def show_privileges(self):
        print('Admin can do:',)
        print(*self.privileges, sep='\n')


class Admin(User):
    def __init__(self, firs_name, last_name):
        super().__init__(firs_name, last_name)
        self.privileges = Priveleges()


new_admin = Admin('zaycev', 'aleksey')
new_admin.greet_user()
new_admin.privileges.show_privileges()