from app import add, sub, mul, div

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(5, 2) == 3

def test_mul():
    assert mul(3, 4) == 12

def test_div():
    assert div(8, 2) == 4
    assert div(5, 0) == "Error: Division by zero"
