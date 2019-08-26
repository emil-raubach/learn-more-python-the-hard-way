from url_search import *

def add_test(urls):
    urls.add('/path/', 'Path')
    urls.add('/path/to/something/', 'Not a path')
    urls.add('/path/to/another/thing/', 'Long Path')

    return urls

def test_match_url(urls):
    assert urls.match_url('/path/') == 'Path'
    assert urls.match_url('/path/to/something') == 'Not at path'
    assert urls.match_url('/path/to/another/thing') == 'Long Path'

def test_url_starts_with(urls):
    urls.add('/path/path/', 'Path Path')
    results = [n.value for n in urls.url_starts_with(test_url)]
    assert results == [
        'Long Path', 
        'Not a path', 
        ]

def test_shortest_url():
    tstrouter = test_match_url()
    test_url = '/path/to/'
    assert tstrouter.shortest_url(test_url).value == 'Not a path'

def test_longest_url():
    tstrouter = test_match_url()
    test_url = '/path/to/'
    assert tstrouter.longest_url(test_url).value == 'Long Path'

def all_tests(urls):
    test_match_url(urls)
    test_url_starts_with(urls)
    test_shortest_url(urls)
    test_longest_url(urls)
    
def test_TSTRouter():
        urls = TSTRouter()
        all_tests(urls)
