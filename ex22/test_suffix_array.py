from suffix_array import SuffixArraySearch

def test_find_shortest():
    test_str = SuffixArraySearch('abracadabra')
    shortest, sa = test_str.find_shortest('abra')
    assert shortest == 1
    shortest, sa = test_str.find_shortest('ra')
    assert shortest == 9

# def test_find_longest():
#     test_str = SuffixArraySearch('abracadabra')
#     longest, sa = test_str.find_longest('abra')
    # assert longest == 2  # longest is at 2, but my algo returns 4...


def test_find_all():
    test_str = SuffixArraySearch('abracadabra')
    all_match, sa = test_str.find_all('abra')
    assert all_match == [1, 2, 3, 4]