roman_numbers= {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1,   
}

def aa_romanos(value:int)-> str:
    """
    Convierte el valor introducido en números romanos
    """
    roman = ""
    for clave, num in roman_numbers.items():
        if num == value:
            roman = clave
            break

        elif value == num * (value // num):
            for _ in range (value // num):
                roman += clave

    return roman

"""
lista_traducciones = []
-Para cada posición, cifra de int, de atras a delante
    -valor = descomponer(posición,cifra)
    -valor_traducido = traducir(valor)
    -añadir valor_traducido a  lista_traducciones

-lista_traducciones_ordenada = darle la vuelta a lista_traducciones
-concatenar lista_traducciones
"""
def descomponer(posición:int,cifra:str)->int:
    return int(cifra) * 10 ** posición

def traducir(valor:int)-> str:
    pass

def a_romanos(number:int)->str:
    lista_traducciones = []
    number_str = str(number)
    reves = number_str[::-1]
    

    for posición, cifra in enumerate(reves):
        valor = descomponer(posición,cifra)
        valor_traducido = traducir(valor)
        lista_traducciones.append(valor_traducido)

    lista_traducciones_inversa = lista_traducciones.reverse()
    num_romano = ""
    for simbolo in lista_traducciones_inversa:
        num_romano += simbolo

    return num_romano


