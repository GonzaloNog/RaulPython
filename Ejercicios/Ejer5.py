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

    elif (command == "suma"):
        nu01 = int(input("ingrese primer numero numero a sumar"))
        nu02 = int(input("ingrese segundo numero numero a sumar"))
        suma (nu01,nu02)    

   

    elif (command == "resta"):
        nu01 = int(input("ingrese primer numero numero a resta"))
        nu02 = int(input("ingrese segundo numero numero a resta"))
        resta (nu01,nu02)

    elif (command == "multiplicacion"):
        nu01 = int(input("ingrese primer numero numero a multiplicar"))
        nu02 = int(input("ingrese segundo numero numero a multiplicar"))
        multiplicacion (nu01,nu02)

    elif (command == "division"):
        nu01 = int(input("ingrese primer numero numero a dividir"))
        nu02 = int(input("ingrese segundo numero numero a dividir"))
        division (nu01,nu02)

         
    
        
    
        