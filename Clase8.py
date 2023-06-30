### Exceptions ###

num1, num2  = 1,2

num1_string = "1"

try:
    print("hola")
    num1  = int(input())
    print('No se produce error')
except:
    print('Se produce error')
else:
    print('todo bien')
finally:
    print('fin')

#exeptions for type
try:
    print(num1 + num2)
    print('todo bien')
except TypeError:
    print('error de tipo')
except ZeroDivisionError:
    print('dividir por 0')

try: 
    print(num1 + num1_string)
    print('No s eproduce error')
except TypeError as error:
    print(error)


