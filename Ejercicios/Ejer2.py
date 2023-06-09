'''
Primero vamos a crear en una lista un registro, el usuario tiene que poner nombre, apellido edad, sueldo bruto anual y en que ciudad vive, 
luego vamos a preguntarle al usuario si quiere abrir una cuenta bancaria nueva, si el usuario escribe que "sí", comprobamos si su sueldo es mayor a 
20.000 euros anuales y si vive en Barcelona en caso de cumplir los requisitos saldrá el mensaje "cuenta completada exitosamente" lo contrario "nos e cumplen
los requisitos para una nueva cuenta"
'''

my_user = list()

my_user.append(input("¿Cual es su Nombre? "))
my_user.append(input(f'Digame su apellido, Sr {my_user[0].capitalize()} '))
print(f'Me alegro de conocerle, Sr {my_user[0].capitalize()}{my_user[1].upper()} ')
my_user.append(int(input (f'Digame su edad, Sr {my_user[1].upper()} ')))
my_user.append(int(input (f'¿cual es su salario anual?, Sr {my_user[1].upper()} ')))
my_user.append(input (f'¿en que ciudad vive?, Sr {my_user[1].upper()} '))
print(f'Estos son sus datos, Sr Nombre: {my_user[0].capitalize()} Apellido: {my_user[1].upper()} Edad: {my_user[2]} Salario: {my_user[3]} Vive en: {my_user[4]}')


pregunta = input("Quiere abrir una cuenta de banco nueva Ingrese si o no ")

if pregunta == "si" or pregunta == "SI":
    if my_user[3] >= 20000:
        if my_user[4].capitalize() == "Barcelona":
            print("Perfecto, su cuenta fue creada")
        else:
            print("lamento informarle que tiene qeu residir en Barcelona para poder crear su cuenta")
    else:
        print("Lamentablemente usted no cuenta con el ingreso suficiente para abrir una cuenta nueva")
elif pregunta == 'no' or pregunta == "NO":
    print("Perfecto. que tenga un buen dia")
else:
    print("tiene que ingresar si o no")

    




