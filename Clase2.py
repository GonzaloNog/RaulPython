### String ###

my_string = 'Mi String'
my_other_string = 'mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + ' ' + my_other_string)

my_new_line_string = "Este es un String\ncon salto de linea" #\n se usa para dejar un renglon 
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulacion" #\t deja una sangria tabulador
print(my_tab_string)

#Formateo

name, surname, age, alias = 'Gonzalo', 'Zeiss', 35, "gon"

print('Mi nombre es {} {} y mi edad es {} y mi alias es {}'.format(name, surname, age, alias)) 
print('Mi nombre es %s %s y mi edad es %d' %(name, surname, age)) #%s string %d entero %f float
print(f'Mi nombre es {name} {surname} y mi edad es {age}')

lenguage = 'Python'
a, b, c, d, e, f = lenguage

#Division

lenguage_slice = lenguage[1:]
print(lenguage_slice)

#Reverse

lenguage_slice = lenguage[:: -1]
print(lenguage_slice)

#print(lenguage.capitalize()) #primera letra en mayuscula
#print(lenguage.upper()) #Todo mayuscula
#print(lenguage.count('t')) #cantidad de un tipo
#print(lenguage.isnumeric()) #Es numerica
#print(lenguage.lower()) #minusculas
#print(lenguage.upper().isupper()) #mayuscula y compueba sie s mayuscula
#print(lenguage.startswith("Py"))

