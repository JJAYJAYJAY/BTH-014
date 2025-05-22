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
            "set": {'a', 1, 3, 2, 87, 65, 43, 23, 12, 45, 67, 89, 90, 100, 200, 300, 400, 500,
                    600, 700, 800, 900, 1300, 410, 1200, 1300, 1400, 1500, 1600,
                    1700, 1800, 1900, 20210, 21200, 2200, 2300, 2400, 2500, 2600,
                    2700, 2800, 2900, 30040},
            "frozenset": frozenset(['a', 1, 3, 2, 87, 65, 43, 23, 12, 45, 67, 89, 90, 100,
                                    200, 300, 400, 500, 600, 700, 800, 900, 1300, 410,
                                    1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900,
                                    20210, 21200, 2200, 2300, 2400, 2500, 2600,
                                    2700, 2800, 2900, 30040]),
            "small_set": {1, 2, 3},
            "small_frozenset": frozenset([1, 2, 3]),
        }

        for name, val in test_cases.items():
            with self.subTest(name=name):
                self.dump_and_check(val, name)


if __name__ == '__main__':
    unittest.main()
