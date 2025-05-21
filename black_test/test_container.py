import platform
import unittest

from black_test.Base_test_class import BaseTestClass

os_name = platform.system()


class TestContainer(unittest.TestCase, BaseTestClass):
    def test_container(self):
        test_cases = {
            "list": [1, 'a', 3, 4, 5, 6],
            "tuple": (1, 2, '*', 43, '1'),
            "dict": {'name': 'Alice', 'age': 21},
            "set": {'a', 1, 3},
            "frozenset": frozenset(['a', 1, 3])
        }

        for name, val in test_cases.items():
            with self.subTest(name=name):
                self.dump_and_check(val, name)


if __name__ == '__main__':
    unittest.main()
