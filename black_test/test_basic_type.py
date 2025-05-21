import hashlib
import platform
import random
import unittest

from lib_pickle import pickle

os_name = platform.system()


class TestBasicType(unittest.TestCase):
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
            with self.subTest(value=name):
                with open(f"res/{os_name}_test_{name}_write.pkl", "wb") as f:
                    pickle.dump(val, f)
                with open(f"res/{os_name}_test_{name}_write.pkl", "rb") as f:
                    self.assertEqual(
                        hashlib.sha256(pickle.dumps(val)).hexdigest(),
                        hashlib.sha256(f.read()).hexdigest()
                    )


if __name__ == '__main__':
    unittest.main()
