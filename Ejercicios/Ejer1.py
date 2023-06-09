'''
Pídale al usuario que ingrese su nombre, su apellido y su edad, estos tienen que estar guardados en una lista, 
luego muestre todos los datos del usuario en un único print usando format
'''
nombre = input("¿Cual es su Nombre?")
apellido = input(f'Digame su apellido, Sr {nombre.capitalize()}')
print(f'Me alegro de conocerle, Sr {nombre.capitalize()}{apellido.upper()}')
edad = int(input (f'Digame su edad, Sr {apellido.upper()}'))

print(f'Estos son sus datos, Sr Nombre: {nombre.capitalize()} Apellido: {apellido.upper()} Edad: {edad}')


