# While 

my_condition = 0

while my_condition <= 20:
    print(my_condition)
    my_condition += 1
else:
    print("Termino el loop")

my_condition = 0

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print('Se detiene la ejecucion')
        break
    print(my_condition)
print("La ejecucion continua")

# For

my_list = [10,2,30,10,34,23,53,2,3,6]

my_condition = 0
while my_condition < len(my_list):
    print(my_list[my_condition])
    my_condition += 1

for element in my_list:
    print(element)
else:
    print('Termina el loop')
