from src.calculator import add, sub, mul, div

def test_add():
    assert add(1,1) == 2  # branch "test3" set back to `assert add(1,1) == 2`
    # alright looks good, let's do a git commit * -m 'adding message to git commit statement'

def test_sub():
    assert sub(1,1) == 0

def test_mul():
    assert mul(1,1) == 1

def test_div():
    assert div(2,1) == 2