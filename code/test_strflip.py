from strflip import strflip

def test_flip_empty_string():
    assert strflip('') == ''

def test_flip_one_char():
    assert strflip('a') == 'a'

def test_flip_repeated_char():
    assert strflip('abca') == 'acba'
