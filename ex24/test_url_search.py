from url_search import URLRouter, URLRouterParser

def test_match_url():
    router = URLRouter()
    router.new_url('/path/', 'Path')
    assert router.match_url('/path/') == 'Path'
    router.new_url('/path/to/something', 'Not a path')
    assert router.match_url('/path/to/') == ""

