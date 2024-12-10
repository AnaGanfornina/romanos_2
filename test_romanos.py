from fromanos import a_romanos

def test_suma_romanos():
    assert a_romanos(20) == "XX","numero incorrecro"
    assert a_romanos(200) == "CC","numero incorrecro"
    assert a_romanos(1) == "I"
    assert a_romanos(500) == "D"