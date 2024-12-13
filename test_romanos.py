from fromanos import a_romanos,descomponer,traducir,a_numeros,traduce_entero,is_valid,RomanNumberError,valida_repeticiones,Roman_Number
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

def test_validar_no_repeticiones_de_3():
    """
    
    V, L, D no se pueden repetir
    """
    assert valida_repeticiones("IIIII") == (False, "I",4)
    assert valida_repeticiones ("XXXX") ==(False, "X",4)
    assert valida_repeticiones ("CCCC") == (False, "C",4)
    assert valida_repeticiones ("MMMM") == (False, "M",4)

def test_validar_no_repeticiones_de_2():
    """
    V, L, D no se pueden repetir
    """
    assert valida_repeticiones("VV") == (False, "V",2)
    assert valida_repeticiones ("LL") ==(False, "L",2)
    assert valida_repeticiones ("DD") == (False, "D",2)

def test_valdar_romano_cuatro_repeticiones():
    with pytest.raises(RomanNumberError) as contexto:
        a_numeros("MCCCCXXII")
    assert str(contexto.value) == "C, solo puede repetirse tres veces"

    with pytest.raises(RomanNumberError) as contexto:
        a_numeros("MMMMCXXII")
    assert str(contexto.value) == "M, solo puede repetirse tres veces"
     
def test_valdar_romano_sin_repeticiones():
    with pytest.raises(RomanNumberError) as ctx_error:
        a_numeros("MCCVV")
    assert str(ctx_error.value) == "V, no puede repetirse"

def test_restas_incorrectas():
    with pytest.raises(RomanNumberError):
        a_numeros("IC")
    with pytest.raises(RomanNumberError):
        a_numeros("VX")
    
def test_no_restas_repetidas():
    with pytest.raises(RomanNumberError):
        a_numeros("XCXC")
def test_no_restas_repetidas_del_mimso_grupo_valor():
    with pytest.raises(RomanNumberError):
        a_numeros("XCXL")
    
def test_no_sumar_mismo_grupo_despues_de_resta():
    with pytest.raises(RomanNumberError):
        a_numeros("XCXXXIII")

def test_no_sumar_mismo_grupo_distinto_valor():
    with pytest.raises(RomanNumberError):
        a_numeros("XCL")

def test_no_restas_contrapeadas():
    with pytest.raises(RomanNumberError):
        a_numeros("IXC")

def test_constructor_entero_clase_Romano():
    rn = Roman_Number(8)

    assert rn.value == 8
    assert rn.representation == "VIII"

def test_consturctor_cadena_clase_Romana():
    rn = Roman_Number("VIII")

    assert rn.value == 8
    assert rn.representation == "VIII"