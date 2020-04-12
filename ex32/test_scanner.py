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
    ('DEF', r'^def'),
    ('NAME', r'^[a-zA-Z][a-zA-Z0-9]*'),
    ('INTEGER', r'^[0-9]+'),
    ('LPAREN', r'^\('),
    ('RPAREN', r'^\)'),
    ('PLUS', r'^\+'),
    ('COLON', r'^:'),
    ('COMMA', r'^,'),
    ('INDENT', r'^\s+')
]

test_scanner = Scanner(token_list)
test_scanner.scan(test_string)