from src.calculator import add, sub, mul, div

def test_add():
    assert add(1,1) == 3  # created branch of "test3" setting the line to be `assert add(1,1) == 3`

def test_sub():
    assert sub(1,1) == 0

def test_mul():
    assert mul(1,1) == 1

def test_div():
    assert div(2,1) == 2