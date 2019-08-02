from tstree import TSTree

def test_set_get():
    names = TSTree()
    names.set('emil', 'myname')
    assert names.get('emil') == 'myname'
    names.set('eddie', 'murphy')
    assert names.get('emil') == 'myname'
    assert names.get('eddie') == 'murphy'
    names.set('bill', 'hicks')
    assert names.get('bill') == 'hicks'
    names.set('eddie', 'money')
    assert names.get('eddie') == 'money'
    assert names.get('eddi') == None

    return names


# def test_find_shortest():
#     pass


# def test_find_longest():
#     pass


def test_find_all():
    things = TSTree()
    things.set('apple', 'Apple')
    things.set('application', 'Application')
    things.set('applaus', 'Applaus')
    things.set('applicant', 'Applicant')
    assert things.find_all('appl') == [
        'Apple',
        'Applaus',
        'Applicant',
        'Application',
    ]
   