
def imprime_operadores():
    """
    Imprime las posibles operaciones matematicas por pantalla
    """
    print("CALCULATUM")
    print("==========")
    print("")
    operadores = ("Sumar","Restar","Multiplicar","Dividir")
    for i in range(4):  
        print(f"{i}. {operadores[i]}")
    
def ask_operation()->str:
    """
    Pide al usuario una operación y devuelve el número identificativo de dicha operación
    """
    user = ""
    while True:
        imprime_operadores()
        user = input("Elige una opción (0 al 3): ") #posteriormente habrá que cambiar del 1 al 4
        opciones = "0123"
        if user in opciones:
            break
        print("Opción incorrecta")
        print("")
    return user



def calculatum()-> int:
    result = 0
    calculation = int(ask_operation())
    first_number = input("Primer número:")
    second_number = input("Segundo número:")

    if calculation == 0:
        result = first_number + second_number
    elif calculation == 1:
        result = first_number - second_number
    elif calculation == 2:
        result = first_number * second_number
    elif calculation == 3:
        result = first_number / second_number
    
        
    return result

    


calculatum()