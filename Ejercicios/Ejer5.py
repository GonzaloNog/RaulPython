def suma(numUno,numDos):
    print(numUno + numDos)

def resta(numUno,numDos):
    print(numUno - numDos)

def multiplicacion(numUno,numDos):
    print(numUno * numDos)

def division(numUno,numDos):
    print(numUno / numDos)       




menu = True
command = "null"

while menu:
    command = input("ingrese datos ")
    if(command == "exit"):
        menu = False
    
    elif(command == "operacion"):
        nu01 = int(input("ingrese primer numero numero "))
        nu02 = int(input("ingrese segundo numero numero "))
        command = input("ingrese tipo de operacion(suma,resta,multiplicacion,division) ")
        if(command == "suma"):
            suma (nu01,nu02) 
        elif (command == "resta"):
            resta (nu01,nu02)
        elif (command == "multiplicacion"):
            multiplicacion (nu01,nu02)
        elif (command == "division"):
            division (nu01,nu02)
        else:
            print("error la oepracion no se encontro")
    else:
        print("error el comando no se encontro")

         
    
        
    
        