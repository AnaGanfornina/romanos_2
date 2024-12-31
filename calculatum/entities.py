from calculatum.roman_funciton import a_romano,a_numeros, RomanNumberError
from typing import Union

class Roman_Number:
    def __init__(self,number:Union[int|str]):
        if type(number) == int:
            self.value = number
            self.representation = a_romano(number)
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
    

