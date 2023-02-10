from twttr import shorten

def test_letters():
    assert shorten("twitter") == "twttr"
    assert shorten("audio") == "d"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("AUDIO") == "D"

def test_numbers_punctuation():
    assert shorten("twitter1") == "twttr1"
    assert shorten("audio!") == "d!"
