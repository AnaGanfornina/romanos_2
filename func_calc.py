from fromanos import a_numeros,RomanNumberError
#from calc_romanos import Operadores

def imprime_operadores():
    """
    Imprime las posibles operaciones matematicas por pantalla
    """
    print("CALCULATUM")
    print("==========")
    print("")
    operadores = ((1,"Sumar","+"),(2,"Restar","-"),(3,"Multiplicar","*"),(4,"Dividir","/"))

    for operador in operadores: 

        print(f"{operador[0]}. {operador[1]}")

    
    
def ask_operation()->str:
    """
    Pide al usuario una operación y devuelve el número identificativo de dicha operación
    """
    user = ""
    while True:
        imprime_operadores()
        user = input("Elige una opción (1 al 4): ") 
        opciones = "1234"
        if user in opciones:
            break
        print("Opción incorrecta")
        print("")

    #user = Operadores.value
    
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

def imput_to_int(number:int)->int:
    """
    Determina si el numero de entrada es transformable en un entero, de no ser asi
    es un número romano y lo traduce. Devuelve un número en ambos casos.
    """
    result = 0
    try: 
        result = int(number)
       
    except ValueError:
        result = a_numeros(number)
    
    return result

def is_valid(num:str)-> bool:
    resutl = True
    try:
        imput_to_int(num)
    except RomanNumberError:
        resutl = False
    return resutl

def ask_input(text:str):
    while True:
        number = input(f"{text}")
        if is_valid(number):
            break
        print("No es un número válido, vuelva a escribirlo")
    return imput_to_int(number)