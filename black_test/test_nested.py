import hashlib
from lib_pickle import pickle
import unittest


class Address:
    def __init__(self, street, city, zip_code):
        self.street = street
        self.city = city
        self.zip_code = zip_code


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address  # 嵌套Address对象


class Testnested(unittest.TestCase):
    def test_nested_dict(self):
        a = {
            "engineering": {
                "manager": {
                    "name": "Alice",
                    "age": 35,
                    "skills": ["Python", "Java", "Leadership"]
                },
                "developers": [
                    {"name": "Bob", "age": 28, "skills": ["Python", "Django"]},
                    {"name": "Charlie", "age": 32, "skills": ["Java", "Spring"]}
                ]
            },
            "marketing": {
                "locate": 'sprck'
            }
        }
        a_pickle1 = pickle.dumps(a)
        a_pickle2 = pickle.dumps(a)
        assert (hashlib.sha256(a_pickle1).hexdigest() == hashlib.sha256(a_pickle2).hexdigest())

    def test_nested_class(self):
        a = Person("John Doe", 30, Address("123 Main St", "Anytown", "12345"))
        a_pickle1 = pickle.dumps(a)
        a_pickle2 = pickle.dumps(a)
        assert (hashlib.sha256(a_pickle1).hexdigest() == hashlib.sha256(a_pickle2).hexdigest())

    def test_nested_list(self):
        a = [[1, 23, 1], 2, [23, [231, [1]]]]
        a_pickle1 = pickle.dumps(a)
        a_pickle2 = pickle.dumps(a)
        assert (hashlib.sha256(a_pickle1).hexdigest() == hashlib.sha256(a_pickle2).hexdigest())


if __name__ == '__main__':
    unittest.main()
