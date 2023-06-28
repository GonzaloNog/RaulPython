### Funciones ###


def my_funtion():
    print('Esto es una funcion')

my_funtion()
my_funtion()

def sum_two_values(first_value,second_value):
    print(first_value + second_value)

def changeNum(num):
    num = 20

numero = 10
changeNum(numero)
print(numero)

def changeNumRet(num):
    return num + 20

numero = changeNumRet(10)
print(numero)

def print_name(name,surname):
    print(f'{name} {surname}')

print_name('gonzalo','zeiss')

print_name(surname = "zeiss", name = 'gonzalo')

def print_name(name: str, surname: str, alias = "sin alias"):
    print(name + surname + ' ' + alias)

print_name('gonzalo', 'zeiss', 'gonza')

