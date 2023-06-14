#Template menu

game = True
comand = "null"

while game:
    comand = input("Ingrese un comando (comandos para lista)) ")
    if(comand == "exit"):
        game = False
        print("Gracias por usar nuestra plataforma. que tenga un buen dia")
    if(comand == "comandos"):
        print("LISTA DE COMANDOS\n\t-exit: salir del programa\n\t-calculadora: calcula dos numeros\n\t\t-suma\n\t\t-resta")
    if(comand == "calculadora"):
        num1 = int(input("Ingrese primer numero "))
        num2 = int(input("Ingrese segundo numero "))
        comand = input("Ingrese operacion ")
        if(comand == "suma"):
            print(num1 + num2)
        if(comand == "resta"):
            print(num1 - num2)
    if(comand == "algo"):
    

