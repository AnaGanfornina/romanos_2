from calculatum.interfaz import muestra_menu,input_numero,input_option,muestra_resultados

def run():
    muestra_menu()
    option = input_option("Selecciona una ",(1,2,3,4))
    num1 = input_numero("Introduce el primer número")
    num2 = input_numero("Introduce el segundo número")
    muestra_resultados(option,num1,num2)
   