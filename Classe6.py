my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {'Nombre':'juan','Apellido':'perez','edad':40}

my_dict = {
    'Nombre':'Gonzalo',
    'Apellido':'zeiss',
    'Edad': 35,
    'Lenguajes':{'Python','Switf','c++'},
    1:1.78
}

print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict['Nombre'])

my_dict['Nombre'] = 'jose'

print(my_dict['Nombre'])

print(my_dict)

my_dict['Calle'] = 'Mi direccion' #si el campo no existe se agrega un nuevo campo

print(my_dict)

del my_dict['Calle'] #elimina un solo elemento del diccionario
print(my_dict)

print('Gonzalo' in my_dict)
print('Nombre' in my_dict)

print('Funciones')
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())