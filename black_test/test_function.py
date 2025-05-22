import platform
import unittest

from black_test.Base_test_class import BaseTestClass

os_name = platform.system()


def function1():
    print('hello world')


def function2(x: int) -> int:
    return x + 1


def function3(x: int) -> bool:
    return x > 1 and x < 100


def function4(x: int):
    if x < 100:
        function4(x + 1)


class TestFunction(BaseTestClass):
    def test_function(self):
        # TC_004
        test_cases = {
            "function1": function1,
            "function2": function2,
            "function3": function3,
            "function4": function4,
        }

        for name, val in test_cases.items():
            with self.subTest(name=name):
                self.dump_and_check(val, name)


if __name__ == '__main__':
    unittest.main()
