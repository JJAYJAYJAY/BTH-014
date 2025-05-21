import hashlib
import unittest

from lib_pickle import pickle


def generator():
    a = []
    for i in range(100):
        a.append(a)
    return a


class TestReference(unittest.TestCase):
    def test_reference(self):
        test_cases = {
            "reference" : generator(),
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
