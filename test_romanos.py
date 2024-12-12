from fromanos import a_romanos,descomponer,traducir,a_numeros,traduce_entero,is_valid,RomanNumberError
import pytest

def _test_simbolos_sencillos():
    assert a_romanos(1) == "I"
    assert a_romanos(500) == "D"

def _test_doble_repetición():
    assert a_romanos(20) == "XX","numero incorrecro"
    assert a_romanos(200) == "CC","numero incorrecro"

def test_descomponer():
    #voy a probar el número 1939, cadena "9391"
    resultado = descomponer(0,"9")
    assert resultado == 9

    resultado = descomponer(1,"3")
    assert resultado == 30

    resultado = descomponer(2,"9")
    assert resultado == 900

    resultado = descomponer(3,"1")
    assert resultado == 1000

def test_traducir():
    assert traducir(9) == "IX"
    assert traducir(30) == "XXX"
    assert traducir(900) == "CM"
    assert traducir(1000) == "M"
    assert traducir(2) == "II"
    assert traducir(800) == "DCCC"
    
def test_romanos_varios():
    assert a_romanos(1939) == "MCMXXXIX"

def test_a_numeros():
    assert a_numeros("MMMCMXCIX") == 3999

    for n in range(1,4000):
        assert a_numeros(a_romanos(n)) == n
    
    assert a_numeros("IV") == 4
    


def test_traduce_entero():
    assert traduce_entero("IX") == 9
    assert traduce_entero("XXX") == 30
    assert traduce_entero("CM") == 900
    assert traduce_entero("M") == 1000
    assert traduce_entero("II") == 2
    assert traduce_entero("DCCC") == 800
    #assert traduce_entero("IIII") != 4
    #with pytest.raises(ValueError):
        #traduce_entero("IIII")


def test_is_valid():
    assert not is_valid("IIII")
    assert is_valid("III")

def test_num_validar_caractereres_romanos():
    with pytest.raises(RomanNumberError) as contexto:
        a_numeros("ZTW")
    
    assert str(contexto.value).endswith("no es un simbolo romano") 