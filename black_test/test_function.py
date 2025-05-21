import hashlib
import unittest

from lib_pickle import pickle


def function1():
    print('hello world')


def function2(x: int) -> int:
    return x + 1


def function3(x: int) -> bool:
    return x > 1 and x < 100


def function4(x: int):
    if x < 100:
        function4(x + 1)


class TestFunction(unittest.TestCase):
    def test_function(self):
        test_cases = {
            "function1" : function1,
            "function2" : function2,
            "function3" : function3,
            "function4" : function4,
        }

        for name,val in test_cases.items():
            with self.subTest(name=name):
                with open(f"res/test_{name}_write.pkl", "wb") as f:
                    pickle.dump(val, f)
                with open(f"res/test_{name}_write.pkl", "rb") as f:
                    self.assertEqual(
                        hashlib.sha256(pickle.dumps(val)).hexdigest(),
                        hashlib.sha256(f.read()).hexdigest()
                    )

if __name__ == '__main__':
    unittest.main()
