
from func_calc import ask_operation,calculation,imput_to_int,is_valid,ask_input
from fromanos import RomanNumberError




def calculatum():
   
    is_exit = "S" #preguntate si estoy hay que refacotrizarlo por un continue
    while is_exit == "S":
        
        operador = int(ask_operation())
        first_number = ask_input("Primer número:")

        second_number = ask_input("Segundo número:")
        
        print(calculation(first_number,second_number,operador))

        is_exit = input("Otra S/N: ").upper()



calculatum()