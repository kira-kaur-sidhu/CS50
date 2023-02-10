from plates import is_valid

def test_alpha():
    assert is_valid("AA") == True
    assert is_valid("A1") == False

def test_characters():
    assert is_valid("CSP502") == True
    assert is_valid("H") == False
    assert is_valid("CSHP502") == False

def test_numbers():
    assert is_valid("OUTATIME") == False
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False

def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("PI3 14") == False
