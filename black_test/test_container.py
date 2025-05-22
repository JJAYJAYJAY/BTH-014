import platform
import unittest

from black_test.Base_test_class import BaseTestClass

os_name = platform.system()


class TestContainer(BaseTestClass):
    def test_container(self):
        # TC_002
        test_cases = {
            "list": [1, 'a', '*', 43, '1', 2, 58],
            "tuple": (1, '*', 43, '1', 2, -2),
            "dict": {'name': 'Alice', 'age': 21},
            "set": {'a', 1, 3, 2, 87},
            "frozenset": frozenset(['a', 1, 3, 2, 87])
        }

        for name, val in test_cases.items():
            with self.subTest(name=name):
                self.dump_and_check(val, name)


if __name__ == '__main__':
    unittest.main()
