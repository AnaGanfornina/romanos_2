roman_numbers= {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1,   
}

def a_romanos(value:int)-> str:
    roman = ""
    for clave, num in roman_numbers.items():
        if num == value:
            roman = clave
        elif value == num * (value / num):
            for _ in range (num ** (value / num)):
                roman += clave 

    return roman

assert a_romanos(1) == "I"
assert a_romanos(500) == "D"

assert a_romanos(20) == "XX","numero incorrecro"
assert a_romanos(200) == "CC","numero incorrecro"