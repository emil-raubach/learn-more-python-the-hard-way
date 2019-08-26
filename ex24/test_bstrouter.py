from url_search import BSTRouter

def test_bstrouter_set_get():
    router = BSTRouter()
    router.add('/path/', 'Path')
    assert router.match_url('/path/') == 'Path'
    router.add('/path/to/something', 'Not a path')
    assert router.match_url('/path/to/something') == 'Not a path'
    router.add('/path/to/another/thing/', 'Long Path')
    assert router.match_url('/path/to/another/thing/') == 'Long Path'

    return router

def test_url_starts_with():
    router = test_bstrouter_set_get()
    result = router.url_starts_with('/path/') 
    assert result == [
        'Path',
        'Not a path',
        'Long Path',
    ]
