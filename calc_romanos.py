
from func_calc import ask_operation,calculation,imput_to_int



def calculatum():
   
    is_exit = "S"
    while is_exit == "S":
        
        
        operador = int(ask_operation())
        first_number = input("Primer número:")
        first_number = imput_to_int(first_number)

        second_number = input("Segundo número:")
        second_number = imput_to_int(second_number)
        
        


        print(calculation(first_number,second_number,operador))

        is_exit = input("Otra S/N: ").upper()



calculatum()