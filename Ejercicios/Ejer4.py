'''
genere un menu con tres opciones.
 - la primera es registro: ingrese en un set un nuevo documento
 - nuevo ingreso, salbo que la persona escriba exit, ingrese todos los documentos que quiera en un nuevo set(si algun documento no esta registrado marque el error al usuario), 
 al finalisar muestre en pantalla los trabajadores que faltaron a la empresa
 - cerrar programa
'''

program = True
comand = "null"
trabajadores = set()
ingresantes = set()
while(program):
    comand = input("Ingrese un comando ")
    
    
    
    if(comand == "exit"):
        program = False
        print('Tenga buen dia')
    
    
    
    
    
    
    if(comand == "registro"):
        registro = input("Ingrese documento sin puntos del empleado nuevo ")
        trabajadores.add(registro)
    
    
    
    
    
    if(comand == "ingreso"):
        ingresantes.clear()
        while(True):
            ingreso = input("Doc empleado entrante (exit salir)")
            if(ingreso == "exit"):
                break
            else:
                ingresantes.add(ingreso)
        faltantes = trabajadores.difference(ingresantes)
        for item in faltantes:
            print(item, " Se encuentra ausente")
    