import re

from scanner import Scanner


# should this be a string or a list of strings like in
# the example?
test_string = """
def add(x, y):
    return x + y
print(add(1, 1))
"""

# Trying so semi-TDD kinda thing here...
token_list = [
    (r'^def', 'DEF'),
    (r'^[a-zA-Z][a-zA-Z0-9]*', 'NAME'),
    (r'^[0-9]+', 'INTEGER'),
    (r'^\(', 'LPAREN'),
    (r'^\)', 'RPAREN'),
    (r'^\+', 'PLUS'),
    (r'^:', 'COLON'),
    (r'^,', 'COMMA'),
    (r'^\s+', 'INDENT')
]
# test fixture - use @pytest.fixture?
test_scanner = Scanner(token_list)


def test_scanner_init():
    result = test_scanner.tokens
    assert result == [(re.compile('^def'), 'DEF'),
                      (re.compile('^[a-zA-Z][a-zA-Z0-9]*'), 'NAME'),
                      (re.compile('^[0-9]+'), 'INTEGER'),
                      (re.compile('^\\('), 'LPAREN'),
                      (re.compile('^\\)'), 'RPAREN'),
                      (re.compile('^\\+'), 'PLUS'),
                      (re.compile('^:'), 'COLON'),
                      (re.compile('^,'), 'COMMA'),
                      (re.compile('^\\s+'), 'INDENT')]
