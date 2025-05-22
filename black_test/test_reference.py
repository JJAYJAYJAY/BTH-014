import unittest

from black_test.Base_test_class import BaseTestClass


def generator():
    a = []
    for i in range(100):
        a.append(a)
    return a


class TestReference(BaseTestClass):
    def test_reference(self):
        # TC_007
        test_cases = {
            "reference": generator(),
        }

        for name, val in test_cases.items():
            with self.subTest(name=name):
                self.dump_and_check(val, name)


if __name__ == '__main__':
    unittest.main()
