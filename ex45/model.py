class Person(object):

    def __init__(self, first_name, last_name, 
                 age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.pet = None


class Pet(object):

    def __init__(self, name, breed, age, dead):
        self.name = name
        self.breed = breed
        self.age = age
        self.dead = dead
