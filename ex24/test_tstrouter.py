from url_search import TSTRouter

def test_match_url():
    tstrouter = TSTRouter()
    tstrouter.new_url('/path/', 'Path')
    assert tstrouter.match_url('/path/') == 'Path'
    tstrouter.new_url('/path/to/something/', 'Not a path')
    assert tstrouter.match_url('/path/to/') == None
    tstrouter.new_url('/path/to/another/thing/', 'Long Path')
    assert tstrouter.match_url('/path/to/another/thing/') == 'Long Path'

    return tstrouter

def test_url_starts_with():
    tstrouter = test_match_url()
    test_url = '/path/'
    results = [n.value for n in tstrouter.url_starts_with(test_url)]
    assert results == [
        'Long Path', 
        'Not a path', 
        ]

def test_shortest_url():
    tstrouter = test_match_url()
    test_url = '/path/to/'
    assert tstrouter.shortest_url(test_url).value == 'Not a path'