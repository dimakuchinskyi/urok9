#Клас урок
#1
try:
    print('start code')
    print(error)
    print('end')
except:
    print('no problems')
print('any code...')

def checker(var):
    if type (var) != str:
        raise TypeError(f'Ми не працюємо з {type(var)}, нам треба str')
    else:
        return var
a = '1234'
checker(a)

class BuildingHouseError(Exception):
    def __str__(self):
        return 'Щось не те, дуже багато і дорого'
def check_matreial_build(amount, limit):
    if amount > limit:
        return 'Достатньо матеріалів!'
    else:
        BuildingHouseError()
print(check_material_build(10, 300))

