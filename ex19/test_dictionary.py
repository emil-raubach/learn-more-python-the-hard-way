from dictionary import Dictionary
from random import randint

# create a mapping of state to abbreviation
def test_set():
    states = Dictionary()
    states.set('Oregon', 'OR')
    states.set('Florida', 'FL')
    states.set('California', 'CA')
    states.set('New York', 'NY')
    states.set('Michigan', 'MI')

    assert states.get('Oregon') == 'OR'
    assert states.get('Florida') == 'FL'
    assert states.get('California') == 'CA'
    assert states.get('New York') == 'NY'
    assert states.get('Michigan') == 'MI'
    assert states.get('Colorado') == None


def test_delete():
    cars = Dictionary()
    cars.set('WRX', 'Subaru')
    cars.set('Cherokee', 'Jeep')
    cars.set('Tacoma', 'Toyota')
    assert cars.get('Cherokee') == 'Jeep'
    cars.delete('Cherokee')
    assert cars.get('Cherokee') == None

def test_hash_key():
    cars = Dictionary()
    index = cars.hash_key('WRX') 
    assert index > 0
    assert index < cars.map.count() # can these tests be combined?
    
if __name__ == "__main__":
    test_set()
    test_delete()