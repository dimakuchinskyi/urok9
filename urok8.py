#Практична робота
#1

class InvalidUsernameError(Exception):
    def __init__(self, username):
        self.username = username
#InvalidLenghtError
#InvalidCharacterError
#

def register_user(username):
    if len(username) < 5:
        raise InvalidUsernameError(username)
    else:
        print('Вас зареєстровано!')
#Приклад використання
try:
    username = input('Введіть ім`я користувача ')
    register_user(username)
except InvalidUsernameError as e:
    print(f'Неправильне ім`я користувача {e.username}'
          f'Мінімум 5 символів.')
