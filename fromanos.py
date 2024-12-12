class RomanNumberError(Exception):
    pass

def descomponer(posición:int,cifra:str)->int:
    return int(cifra) * 10 ** posición

def traducir(valor:int)-> str:
    simbolos = {
        0:'', 1: 'I', 2:'II', 3:'III', 4: 'IV', 5: 'V', 6:'VI', 7: 'VII', 8: 'VIII', 9:'IX',
        10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50:'L', 60:'LX', 70:'LXX', 80:'LXXX', 90:'XC',
        100: 'C', 200: 'CC', 300: 'CCC', 400:'CD', 500:'D', 600:'DC', 700:'DCC', 800:'DCCC', 900:'CM',
        1000:'M', 2000:'MM', 3000:'MMM'
    }
    return simbolos[valor]


def a_romanos(number:int)->str:
    lista_traducciones = []
    number_str = str(number)
    reves = number_str[::-1]
    

    for posición, cifra in enumerate(reves):
        valor = descomponer(posición,cifra)
        valor_traducido = traducir(valor)
        lista_traducciones.append(valor_traducido)

    lista_traducciones_inversa = lista_traducciones[::-1]
    num_romano = ""
    for simbolo in lista_traducciones_inversa:
        num_romano += simbolo

    return num_romano

def traduce_entero(simbolo:str)-> int:
    """
    Traduce un simbolo a numero romano, si no puede devuelve un ValueError
    """
    simbolos = {
        0: '', 1: 'I', 2:'II', 3:'III', 4: 'IV', 5: 'V', 6:'VI', 7: 'VII', 8: 'VIII', 9:'IX',
        10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50:'L', 60:'LX', 70:'LXX', 80:'LXXX', 90:'XC',
        100: 'C', 200: 'CC', 300: 'CCC', 400:'CD', 500:'D', 600:'DC', 700:'DCC', 800:'DCCC', 900:'CM',
        1000:'M', 2000:'MM', 3000:'MMM'
    }
    traduccion = 0

    for clave,valor in simbolos.items():
        if simbolo == valor:
            traduccion = clave
            break

    return traduccion

def is_valid(simbolo:str)->bool:
    """
    Predicado que devuelve true si el número es válido
    """
    return traduce_entero(simbolo) != 0

def a_numeros(simbolo:str)-> str:
    """
    Traduce numeros romanos a numeros enteros.
    """
    total = 0
    num_prev = 0
    
    for signo in simbolo:
        valor = traduce_entero(signo)
        
        if valor == 0:
            raise RomanNumberError(f"{signo} no es un simbolo romano") #esto estaría bien pasarlo a una función
        
        if num_prev >= valor or num_prev == 0:
            total += valor
        else:
            otro_valor = valor - num_prev * 2
            total += otro_valor
            
        num_prev = valor
    
    return total

def esta_en_racha(haystack,neddle:str,racha:int)->bool:
    cont = 0
    if len(haystack) >= racha:
        for el in haystack:
            if el == neddle:
                cont += 1
                if cont == racha:
                    break
            else:
                cont = 0
    else:
        cont = 0
    return cont == racha

def valida_repeticiones(num_roman:str)->bool:
    """
    Predicado que comprueba que I, X, C, M  no se repitan más de 3 veces
    al igual que V, L, D 
    """
    no_repeat = "IXCM"
    en_racha = True
    for caracter in no_repeat:
        if esta_en_racha(num_roman, caracter, 4):
            en_racha = False
            break
            
    return en_racha  
    

def program():
    user_answer = input("Introduzca el número a traducir: ")
    result = 0
    try: 
        int(user_answer)
        result = a_romanos(int(user_answer)) #esto es probable hacerlo con un try except
    except ValueError:
        result = a_numeros(user_answer)
    
    return result


