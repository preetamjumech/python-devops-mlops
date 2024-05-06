from hello import add, subtract, multiply, divide

def test_add():
    assert add(3,5) == 8

def test_subtract():
    assert subtract(5,3) ==2

def test_multiply():
    assert multiply(5,5) == 25

def test_divide():
    assert divide(10,2) == 5

