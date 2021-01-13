from models import connect, load_schema, Person, Pet


connect(':memory:')
load_schema('ex45.sql')


def test_create():
    p = Person('Emil', 'Raubach', 46)
    p.create()
    p.read()
