from calculatum.entities import Roman_Number
from calculatum.roman_funciton import RomanNumberError
def muestra_menu():
    """
    Presenta el menú por pantalla
    """
    print("CALCULATUM")
    print("==========")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicación")
    print("4.División\n")

def input_option(msg:str,options: tuple):
    """
    Función que recibe del usuario la opcion que debe escoger
    """
    opt = ""
    options = tuple(map(str,options))
    while True:
        opt = input(f"{msg}: ")
        if opt in options:
            break
        print(f"Introduce un valor de los siguientes{options}")

    return opt


def input_numero(msg: str)-> Roman_Number:
    while True:
        candidato  = input(f"{msg}:")
        try:
            res = Roman_Number(int(candidato) if candidato.isdigit() else candidato)
            break
        except:
            print("Escribe un entero o romano válido")
    
    return res

def muestra_resultados(option:int,num1:Roman_Number,num2:Roman_Number):
    if option == "1":
        ops = "+" 
        res = num1 + num2
    elif option == "2":
        ops = "-" 
        res = num1 - num2
    elif option == "3":
        ops = "*" 
        res = num1 * num2
    else:
        ops = "÷" 
        res = num1 // num2
    
    print(f"Resultado: {num1} {ops} {num2} = {res}")


