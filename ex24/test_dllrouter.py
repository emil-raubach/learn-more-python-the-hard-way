from url_search import DLLRouter

def test_add():
    router = DLLRouter()
    router.add('/path/', 'Path')
    assert router.urls.get(0).value == 'Path'
    router.add('/path/to/something', 'Not a path')
    assert router.urls.get(1).value == 'Not a path'
    router.add('/path/to/another/thing', 'Long Path')
    assert router.urls.get(2).value == 'Long Path'

    return router

def test_match_url():
    router = test_add()
    assert router.match_url('/path/') == 'Path'
    assert router.match_url('/path/to/another/thing') == 'Long Path'
    assert router.match_url('/path/to/something') == 'Not a path'
    assert router.match_url('/this/should/fail/') == None

def test_url_starts_with():
    router = test_add()
    assert router.url_starts_with('/p') == [
        'Path',
        'Not a path',
    ]