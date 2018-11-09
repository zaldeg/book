from user import User


class Privileges:
    def __init__(self):
        self.privileges = ['разрешено добавлять сообщение', 'разрешено удалять сообщения',
                           'разрешено банить пользователей']

    def show_privileges(self):
        print('Admin can do:',)
        print(*self.privileges, sep='\n')


class Admin(User):
    def __init__(self, firs_name, last_name):
        super().__init__(firs_name, last_name)
        self.privileges = Privileges()