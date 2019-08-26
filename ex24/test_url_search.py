from url_search import URLRouter

# need to align - in one case I test the value, 
# in the other I test the key.
def test_match_url():
    router = URLRouter()
    router.add('/path/', 'Path')
    assert router.match_url('/path/') == 'Path'
    router.add('/path/to/something/', 'Not a path')
    assert router.match_url('/path/to/') == None
    router.add('/path/to/another/thing/', 'Long Path')
    assert router.match_url('/path/to/another/thing/') == 'Long Path'

    return router

def test_url_starts_with():
    router = test_match_url()
    test_url = '/path/'
    assert router.url_starts_with(test_url) == [
        '/path/', 
        '/path/to/something/', 
        '/path/to/another/thing/'
        ]
        
# def test_best_match_url():
#     router = test_match_url()
#     test_url = '/path/to/something/bigger/'
#     assert router.best_match_url(test_url) == '/path/'


# def test_shortest_url():
#     router = test_match_url()
#     test_url = '/path/to/something/'
#     assert router.shortest_url(test_url) == '/path/'