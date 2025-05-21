import platform
import random
import unittest

from black_test.Base_test_class import BaseTestClass

os_name = platform.system()


class TestBasicType(unittest.TestCase, BaseTestClass):
    def test_basic_type(self):
        test_cases = {
            "int": 1,
            "float": 1.0,
            "high_float": random.uniform(1.0, 1000000.0),
            "str": "hello",
            "byte": b"hello",
            "None": None,
            "bool": True,
        }

        for name, val in test_cases.items():
            with self.subTest(name=name):
                self.dump_and_check(val, name)


if __name__ == '__main__':
    unittest.main()
