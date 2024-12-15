
from func_calc import ask_operation,calculation

def calculatum():
   
    is_exit = "S"
    while is_exit == "S":
        
        
        operador = int(ask_operation())
        first_number = int(input("Primer número:"))
        second_number = int(input("Segundo número:"))

        print(calculation(first_number,second_number,operador))

        is_exit = input("Otra S/N: ").upper()


    
        
    
    


calculatum()