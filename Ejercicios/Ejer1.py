'''
Pídale al usuario que ingrese su nombre, su apellido y su edad, estos tienen que estar guardados en una lista, 
luego muestre todos los datos del usuario en un único print usando format
'''
#sin lista
nombre = input("¿Cual es su Nombre?")
apellido = input(f'Digame su apellido, Sr {nombre.capitalize()}')
print(f'Me alegro de conocerle, Sr {nombre.capitalize()}{apellido.upper()}')
edad = int(input (f'Digame su edad, Sr {apellido.upper()}'))

print(f'Estos son sus datos, Sr Nombre: {nombre.capitalize()} Apellido: {apellido.upper()} Edad: {edad}')


#con lista
my_user = list()

my_user.append(input("¿Cual es su Nombre? "))
my_user.append(input(f'Digame su apellido, Sr {my_user[0].capitalize()} '))
print(f'Me alegro de conocerle, Sr {my_user[0].capitalize()}{my_user[1].upper()} ')
my_user.append(int(input (f'Digame su edad, Sr {my_user[1].upper()} ')))
print(f'Estos son sus datos, Sr Nombre: {my_user[0].capitalize()} Apellido: {my_user[1].upper()} Edad: {my_user[2]}')






