from calc_romanos import calculation

def test_calculo_operaciones_simples_int():
    assert calculation(5,5,0) == 10
    assert calculation(5,3,1) == 2
    assert calculation(2,2,2) == 4
    assert calculation(10,2,3) == 5
    

    