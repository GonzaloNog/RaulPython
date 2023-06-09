'''
Primero vamos a crear en una lista un registro, el usuario tiene que poner nombre, apellido edad, sueldo bruto anual y en que ciudad vive, 
luego vamos a preguntarle al usuario si quiere abrir una cuenta bancaria nueva, si el usuario escribe que "sí", comprobamos si su sueldo es mayor a 
20.000 euros anuales y si vive en Barcelona en caso de cumplir los requisitos saldrá el mensaje "cuenta completada exitosamente" lo contrario "nos e cumplen
los requisitos para una nueva cuenta"
'''

nombre, apellido, edad, sueldo, ciudad = input("Digame su nombre "), input("Digame su apellido "), int(input("Digame su edad ")),int(input("¿Cual es su salario anual? ")),input("¿En que ciudad vive? ")
print(f'Su nombre es {nombre.capitalize()} {apellido.upper()} su edad es {edad} su salario anual es {sueldo} vive en {ciudad}')
#my_list = [nombre, apellido, edad, sueldo, ciudad]
pregunta = str(input (f'¿Quiere abrir una nueva cuenta?, Sr {apellido.upper()}'))



#if 1 > 0:

comando = input("Ingrese si o no")

if comando == "si" or comando == "SI":
    print("confirmo")
elif comando == 'no' or comando == "NO":
    print("denego")
else:
    print("tiene que ingresar si o no")

    #




