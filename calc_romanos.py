
from func_calc import ask_operation,calculation,imput_to_int,is_valid,ask_input
from enum import Enum

"""
class Operadores(Enum):
    SUMA = "1"
    RESTA = "2"
    MULTIPLICACION = "3"
    DIVISION = "4"
"""




def to_print_result(first:int,operation:int,second:int):

    result = calculation(first,second,operation)

    print(f"{first} {operation} {second} = {result}")


def calculatum():

    
   
    other_operation = "S" 
    while other_operation == "S":
        
        operador = int(ask_operation())
        first_number = ask_input("Primer número:")

        second_number = ask_input("Segundo número:")

        to_print_result(first_number,operador,second_number)
        
        
        other_operation = input("Otra S/N: ").upper()



#calculatum()