from typing import Union

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
    #cadena = ""
    number_str = str(number) 
    reversed_number_str = number_str[::-1]

    i = 0
    lista = []
    tripleta = [0,0,0]
    
    for index,item in enumerate(reversed_number_str):
        tripleta[i] = item
        i += 1
        if i == 3:
            lista.append(tripleta)
            tripleta = [0,0,0]
            i = 0
        elif index == len(reversed_number_str)-1:
            lista.append(tripleta)

    print(lista)

    

def a_romano(number:int)->str:
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

def puede_restar(lista_restas:list, resta:int)->bool:
    """
    Predicado que devuelve True si ve que puede restar comparandolo 
    con la lista de restas
    """
    try:
        ultima_resta = str(lista_restas[-1])
    except IndexError:
        return True
    
    resta_acutal = str(resta)
    result = True
    if len(ultima_resta) <= len(resta_acutal):
        result = False
    return result

def puede_sumar(valor:int,last:int)->bool:
    """
    Predicado que devuelve true si la longitud de valor es menor
    que la longitud de last
    """
    return len(str(valor)) < len(str(last))


def a_numeros(simbolo:str)-> str:
    """
    Traduce numeros romanos a numeros enteros.
    """
    total = 0
    num_prev = 1001
    substract = lambda x:x - (2 * num_prev)
    restas_validas = ((1,5),(1,10),(10,50),(10,100),(100,500),(100,1000))
    restas_realizadas = []
    ha_restado = False
    ultima_resta = 0

    valida,char,limit = valida_repeticiones(simbolo)
    if not valida:
        raise RomanNumberError(f"{char}, {'solo' if limit == 4 else 'no'} puede repetirse{' tres veces' if limit == 4 else ''}")
        
    for signo in simbolo:
        #El signo existe en el numero romano(simbolo)
        valor = traduce_entero(signo)
        
        if valor == 0:
            raise RomanNumberError(f"{signo} no es un simbolo romano") 
        
        if ha_restado and valor > num_prev:
            #Resta contrapeda
            raise RomanNumberError("Restas anidadas")
        
        elif ha_restado:
            #Suma inmediatamente posterior a una resta
            if puede_sumar(valor,ultima_resta):
                        total += valor
                        ha_restado = False 
                        
            else:
                raise RomanNumberError("Suma  después de resta no permitida")
                
        elif valor > num_prev: 
            #Resta normal      
            if (num_prev,valor) in restas_validas:
                ultima_resta = valor - num_prev
                """
                if not puede_restar(restas_realizadas, ultima_resta):
                    raise RomanNumberError("No se permiten restas duplicasas")
                
                restas_realizadas.append(ultima_resta)
                """
                total += substract(valor)
                ha_restado = True
            else:
                raise RomanNumberError("f{num_prev},{valor} resta no permitida") 
        else:
            #Suma normal
            total += valor
                
        num_prev = valor
    
    return total

def esta_en_racha(haystack,neddle:str,racha:int)->bool:
    """
    Devuelve True si la aguja esta en una racha del número indicado
    """
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
    y que  V, L, D  no se repitan mas de dos
    """
    no_repeat = [("I",4),("X",4),("C",4),("M",4),
                 ("V",2),("L",2),("D",2)]
    en_racha = True
    for caracter, limit in no_repeat:
        if esta_en_racha(num_roman, caracter, limit):
            en_racha = False
            break
            
    return en_racha,caracter,limit
    

def translator(number:int|str):
    
    result = 0
    try: 
        int(number)
        result = a_romanos(int(number)) #esto es probable hacerlo con un try except
    except ValueError:
        result = a_numeros(number)
    
    return result


class Roman_Number:
    def __init__(self,number:Union[int|str]):
        if type(number) == int:
            self.value = number
            self.representation = a_romanos(number)
        elif type(number) == str:
            self.value = a_numeros(number)
            self.representation = number
        else:
            raise RomanNumberError("Solo admitimos int o str")


    def __str__(self) -> str:
        return f"{self.representation}"
    
    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other,self.__class__):
            return False
        return self.value == other.value
    def __hash__(self) -> int:
        return hash(self.value)
    
    def __add__(self, other:object):
        """
        1.Validar el tipo de other
        2.Realizar suma
        3.Devolver romano
        """
        """
        #Método de calros
        if not isinstance(other,int) and not isinstance(other,self.__class__):
            raise TypeError(f" '+' not supported between instances of {self.__class__.__name__} and {other.__class__}")
        
        return Roman_Number(self.value + other.value)
        """
        
        if isinstance(other,int):
            number_value = other
        elif isinstance(other,self.__class__):
            number_value = other.value
        else:
            raise TypeError(f" '+' not supported between instances of 'Roman_Number' and {other.__class__}")
    
        suma = self.value + number_value
        return  Roman_Number(suma)
       
    def __radd__(self, other: object): # Para trabajar con sumas inversas
        return self.__add__(other)
    
    def __sub__(self, other: object): #Para restar
        result = 0
        
        if isinstance(other, self.__class__):
            result = self.value - other.value
            if result < 0:
                raise ValueError("There is no roman representation for the number {result}")
        
        elif isinstance(other,int):
            result = self.value - other.value
            if result < 0:
                raise ValueError("There is no roman representation for the number {result}")
        else:
            raise TypeError(f" '-' not supported between instances of 'Roman_Number' and {other.__class__}")
    
        
        return  Roman_Number(result)
    
    def __rsub__(self, other: object):
        """
        result = 0
        
        if isinstance(other, self.__class__):  #Este if podría ser reduncante porque ya comprobamos qeu es un Roman Number o no en el sub
            result = other.value - self.value
            if result < 0:
                raise ValueError("There is no roman representation for the number {result}")
        
        if isinstance(other,int):
            result = other - self.value 
            if result < 0:
                raise ValueError("There is no roman representation for the number {result}")
        else:
            raise TypeError(f" '-' not supported between instances of 'Roman_Number' and {other.__class__}")
        
        return  Roman_Number(result)
        """
        if isinstance(other,int):
            number_value = other
        else:
            raise TypeError(f" '-' not supported between instances of 'Roman_Number' and {other.__class__}")
        
        roman_number_value = Roman_Number(number_value) #convertimos en un romano el int que nos llega de other
        
        return roman_number_value - self

    def __mul__(self, other: object): # Para las multiplicaciones

        if isinstance(other,int):
            number_value = other
        elif isinstance(other,self.__class__):
            number_value = other.value
        else:
            raise TypeError(f" '*' not supported between instances of 'Roman_Number' and {other.__class__}")
    
        multiply = self.value * number_value
        return  Roman_Number(multiply)
    
    def __rmul__(self, other: object): #Multiplicación inversa
        return  self.__mul__(other)
    
    def __truediv__(self, other: object): # División con decimales
        pass

    def __floordiv__(self, other: object): # División entera
        if isinstance(other,int):
            number_value = other
        elif isinstance(other,self.__class__):
            number_value = other.value
        else:
            raise TypeError(f" '//' not supported between instances of 'Roman_Number' and {other.__class__}")
        division = self.value // number_value
        return  Roman_Number(division)
    
    
    def __rfloordiv__(self, other: object): # División entera inversa
        if isinstance(other,int):
            number_value = other

        elif isinstance(other,self.__class__):
            number_value = other.value
        else:
            raise TypeError(f" '//' not supported between instances of 'Roman_Number' and {other.__class__}")

        return Roman_Number(number_value // self.value)
    
    def __mod__(self, other: object): # Para calcular el resto
        if isinstance(other,int):
            number_value = other
        elif isinstance(other,self.__class__):
            number_value = other.value
        else:
            raise TypeError(f" '%' not supported between instances of 'Roman_Number' and {other.__class__}")
        
        module = self.value % number_value
        return Roman_Number(module)
    def __rmod__(self, other: object): # Para calcular el resto inverso
        if isinstance(other,int):
            number_value = other
        elif isinstance(other,self.__class__):
            number_value = other.value
        else:
            raise TypeError(f" '%' not supported between instances of 'Roman_Number' and {other.__class__}")
        
        module = number_value % self.value
        return Roman_Number(module)
    
    
    def __lt__(self, other: object) -> bool:  # menor que/  less than
        return self.value < other.value
    
    def __le__(self,other: object) -> bool: # menor o igual/ lesss or or equal than 
        return self.value <= other.value
    
    def __gt__(self,other: object) -> bool: # mayor que /greater than
        return self.value > other.value
    
    def __ge__(self,other: object) -> bool: # mayor o igual /greater or equal than
        return self.value >= other.value

    def __ne__(self, other: object) -> bool: # distinto de /not  equal
        return self.value != other.value
    
