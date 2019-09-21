import tr

def test_translate():
    test_input = "ttyyhhxxaa"
    results = tr.translate('t', 'X', test_input)
    assert results == "XXyyhhxxaa"

def test_tr_cs():
    results = tr.main(['-cs', 't', 'X'], 'ttyyhhxxaa')
    assert results == "XXyyhhxxaa"