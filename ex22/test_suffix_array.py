from suffix_array import SuffixArraySearch

def test_find_shortest():
    test_str = SuffixArraySearch('abracadabra')
    shortest, sa = test_str.find_shortest('abra')
    assert shortest == 1

def test_find_longest():
    test_str = SuffixArraySearch('abracadabra')
    longest, sa = test_str.find_longest('abra')
    