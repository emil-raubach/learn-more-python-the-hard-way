from regex import RegEx

# fixture
regex_obj = RegEx()


def test_pass():
    test_string = 'ABRACADABRA'
    rv = regex_obj.transduce(test_string)
    assert rv == ['ACCEPT',
                  'ACCEPT',
                  'ACCEPT',
                  'ACCEPT',
                  'ACCEPT',
                  'ACCEPT',
                  'ACCEPT',
                  'ACCEPT',
                  'ACCEPT',
                  'ACCEPT',
                  'ACCEPT',
                  ]
    print(f'The return value is {rv}.')


def test_fail_first():
    test_string = '12345'
    rv = regex_obj.transduce(test_string)
    assert rv == ['REJECT',
                  'REJECT',
                  'REJECT',
                  'REJECT',
                  'REJECT',
                  ]
    print(f'The return value is {rv}.')


def test_fail_third():
    test_string = 'AZ345'
    rv = regex_obj.transduce(test_string)
    assert rv == ['ACCEPT',
                  'ACCEPT',
                  'REJECT',
                  'REJECT',
                  'REJECT',
                  ]
    print(f'The return value is {rv}.')