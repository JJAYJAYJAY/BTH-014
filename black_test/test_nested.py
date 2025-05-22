import platform
import unittest

from black_test.Base_test_class import BaseTestClass

os_name = platform.system()


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


class Testnested(BaseTestClass):
    def test_nested(self):
        # TC_006
        test_cases = {
            "nested_dict": {
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
            },
            "nested_class": Person("John Doe", 30, Address("123 Main St", "Anytown", "12345")),
            "nested_list": [[1, 23, 1], 2, [23, [231, [1]]]]
        }

        for name, val in test_cases.items():
            with self.subTest(name=name):
                self.dump_and_check(val, name)


if __name__ == '__main__':
    unittest.main()
