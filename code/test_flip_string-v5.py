from flip_string import flip_string

def test_flip_one_char():
    assert flip_string('a') == 'a'

def test_flp_two_charsi():
    assert flip_string('ab') == 'ba'

def test_flip_palindrome():
    assert flip_string('aba') == 'aba'
