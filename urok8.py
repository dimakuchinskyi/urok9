#Практична робота
#1
'''
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
'''
#2
'''
class InvalidPasswordError(Exception):
    def __init__(self, password):
        self.password = password
        super().__init__("Invalid password")

def validate_password(password):
    # Перевірка на умови пароля
    if len(password) < 8 or not any(char.isdigit() for char in password):
        raise InvalidPasswordError(password)

# Приклад використання
try:
    password = input("Введіть пароль: ")
    validate_password(password)
    print("Пароль валідний!")
except InvalidPasswordError as e:
    print(f"Помилка перевірки пароля: {e.password} є неправильним.")
    '''
#3
class InvalidFileFormatError(Exception):
    def __init__(self, filename):
        self.filename = filename
        super().__init__(f"Invalid file format: {filename}")


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except IsADirectoryError:
        print(f"Invalid file: {filename} is a directory")
    except PermissionError:
        print(f"Permission denied: {filename}")
    except UnicodeDecodeError:
        raise InvalidFileFormatError(filename)


# Приклад використання
try:
    content = read_file("text.txt")
    print(content)
except InvalidFileFormatError as e:
    print(e)
