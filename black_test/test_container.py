import hashlib
import unittest

from lib_pickle import pickle


class TestContainer(unittest.TestCase):
    def test_container(self):
        test_cases = {
            "list" : [1, 'a', 3, 4, 5, 6],
            "tuple": (1, 2, '*', 43, '1'),
            "dict": {'name': 'Alice', 'age': 21},
            "set":{'a', 1, 3},
            "frozenset":frozenset(['a', 1, 3])
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
