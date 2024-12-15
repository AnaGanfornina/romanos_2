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


def calculation(first:int,second:int,operador)-> int:
    """
    Función que recibe un primer, un segudo número y calcula según el operador
    No comprueba que las operaciones sean posibles
    """
    result = 0

    if operador == 0:
            result = first + second
    elif operador == 1:
            result = first - second
    elif operador == 2:
            result = first * second
    elif operador == 3:
            result = first / second
    return result