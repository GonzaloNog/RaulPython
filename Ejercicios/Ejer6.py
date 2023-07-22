'''
1 - Crear un menu(quit,list,registro,usuarios,login) (el menu tiene que estar en una funcion llamada main())
2 - quit: terminar el programa
3 - list una lista ordenada de todos los comandos y una descripcion

Funciones
4 - registro primero ingresa el nombre y se comprueban las siguientes cosas 
        - no puede contener espacios 
        - tiene que tener almenos 6 caracteres
        - no puede estar repetido
        se se cumple
        - ingrese la clave nueva
        - la clave no puede contener espacios
        - la clave tiene que tneer almenos 4 caracteres

5 - Mostrar usuarios
    mostrar todos los usuarios en una lista

6 - logue 
    - el usuario ingresa usuario y clave
    - si el usuario se encontro y la clave coincide nos da la vienvenida al sistema
    - si el usuario esta bien pero la clave mal nos dice que la clave esta errada
    - si el usuario no se encuentra nos dice que no esta registrado ningun usuario con ese nombre 
'''


'''

#registro = set()

def main():

'''
usuario = {} 
def Registro():
    Nombre = input("Ingrese su nombre ")
    if (Nombre.count(' ')):
        print("No debe contener espacios")
        return
        
    elif  (len(Nombre) < 6 ):
        print ("tiene que tener almenos 6 caracteres")
        return
    
    if(Nombre in usuario):
        print("este nombre ya existe, pruebe otro nombre")
        return
   
    Pass = input("Ingrese una clave nueva ")
    if (Pass.count(' ')):
        print("No debe contener espacios")
        return
    
    elif (len(Pass) < 4 ):
        print ("la clave tiene que tener almenos 4 caracteres")
        return
    usuario[Nombre] = Pass

def mostrarUsuarios ():
    print('\n---USUARIOS---')
    for element in usuario:
        contenido  = usuario [element]
        print(f"\t-nombre de ususario: {element} clave:{contenido}")



def Main():
    menu = True
    comand = "null"
    while(menu):
        comand = input("ingrese un comando ")
        if (comand == "exit"):
            menu = False
            print("tenga un buen dia ")

        elif (comand == "list"):
            print("List\nComandos:\n\tRegistro: Puedes registrar un nuevo usuario\n\tUsuarios: Puedes crearte un nuevo perfil\n\tLogin: puedes crear una contraseña nueva")    
            
        elif (comand == "registro"):
            Registro()
        
        elif (comand == "usuarios"):
            mostrarUsuarios ()

        elif (comand == "login"):
            print("login")
         
        else:
            print("comando no encontrado" )

Main()



 
        



        




    



  




