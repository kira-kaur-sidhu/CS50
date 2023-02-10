from bank import value

def test_hello():
    assert value("hello Sam!") == 0
    assert value("Hello") == 0

def test_hname():
    assert value("hi Sam!") == 20
    assert value("Hi!") == 20

def test_other():
    assert value ("Morning Sam!") == 100
    assert value ("whatsup") == 100
