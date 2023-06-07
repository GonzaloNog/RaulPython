'''
Raul te paso una tareita para que practiques, vas a tener que crear 3 variables distintas, una para tu nombre, otra para tu apellido y otra para tu edad,
vas ponerles algun contenido, luego vas a imprimir los tipos de dato de cada variable,
luego vas a mostrar los datos usando alguno de los tres metodos de formateo que vimos, 
al final de todo quiero que muestres tu nombre pero todo en mayusculas

name, surname, age = 'raul', 'rengifo', 40

print(f'Mi nombre es {name.capitalize()} {surname} y mi edad es {age}')

print(type(name))
print(type(surname))
print(type(age))
'''

#Input 
"""
print("Como te llamas", end=" ")#end trabajar sobr ela misma linea 
nombre = input()
print(f'Me alegro de conocerte, {nombre}')


nombre = input("Como te llamas? ")
print(f'Me alegro de conocerte, {nombre}')

#Ejemplo de error
cantidad = input("Digame su numero favorito: ")
print(f'la mitad de su numero favorito es {cantidad/2}')

cantidad = float(input("Digame su numero favorito: "))
print(f'la mitad de su numero favorito es {cantidad/2}')
"""

nombre = input("Digame su nombre ")
apellido = input(f'Digame su apellido, Sr{nombre}: ')
print(f'Me alegro de conocerle, {nombre}{apellido}.')
