# Make a general `Model()` class that all models inherit from?
# What would they inherit?
# Start by making classes for data types (e.g., integer, real, text, etc.)
import sqlite3


CONN = None


def connect(db):
    global CONN
    CONN = sqlite3.connect(db)


def load_schema(schema):
    cur = CONN.cursor()
    script = open(schema).read()
    cur.executescript(script)
    CONN.commit()


class Person(object):

    def __init__(self, first_name, last_name, age):
        self.pk = None
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def create(self):
        cur = CONN.cursor()
        cur.execute('''insert into person (first_name, last_name, age)
                    values (?, ?, ?)''',
                    (self.first_name, self.last_name, self.age))
        self.pk = cur.lastrowid
        CONN.commit()
        cur.close()

    # UPDATE - could put general stuff in a super class?
    def update(self):
        cur = CONN.cursor()
        cur.execute(
            'update person set first_name=?, last_name=?, age=? where id=?',
            (self.first_name, self.last_name, self.age, self.pk))
        CONN.commit()
        cur.close()

    def delete(self):
        pass

    def read(self):
        cur = CONN.cursor()
        cur.execute('select first_name, last_name, age from person where id=?', (self.pk,))
        row = cur.fetchone()
        print(row)
        cur.close()


class Pet(object):

    def __init__(self, id, name, breed, age, dead):
        self.id = id
        self.name = name
        self.breed = breed
        self.age = age
        self.dead = dead