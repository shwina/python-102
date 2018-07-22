from flip_string import flip_string

def test_flip_mario():
    assert flip_string('mario') == 'oiram'

def test_flip_luigi():
    assert flip_string('luigi') == 'igiul'

def test_flip_samus():
    assert flip_string('samus') == 'sumas'
