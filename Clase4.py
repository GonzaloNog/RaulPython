#Operadores logicos

var_bool = True
print(var_bool)

print(5 > 4)
print(not(5 > 4))

print("aaa" > "Baa")

print(3 > 4 or 5 > 3)
print(3 > 4 and 5 > 3)

#Condicionales 

if 3 > 4:
    print("VERDADERO")
elif 4 > 5:
    print("VERDADERO 2")
else:
    print("FALSO")

#Listas
my_list = list()
my_other_list = []

print(type(my_list))
print(type(my_other_list))

my_list = [1,1,3,4,5,6,7,8]

print(my_list.count(1)) #cuenta la cantidad de veces que se repite un valor
print(len(my_list))#cantidad de elementos

list_user = ['gonzalo','zeiss','gonza',27]

name, lastname, apodo, age = list_user

print(lastname)

funcion_list = ['hola','casa','chau','perro']

funcion_list.append("tres")#Agrega al final

print(funcion_list)

funcion_list.insert(1, "perro")# en la posicion que se quiera

print(funcion_list)

funcion_list.remove("perro")#elimina el primer elemento encontrado

print(funcion_list)

my_string = funcion_list.pop(2)

print(my_string)

print(funcion_list)

new_list = funcion_list.copy()

print(funcion_list[2])#nos deja ver el valor de un elemento en concreto 

funcion_list.sort()#ordena la lista

print(funcion_list)

del funcion_list[1] #elimina el elemento sin retorno como con el pop()

funcion_list.clear() #borra el contenido 
