import hashlib
import json
import unittest
from collections import Counter, OrderedDict, defaultdict, deque, namedtuple
from datetime import datetime
from pathlib import Path

from lib_pickle import pickle


class TestMoudle(unittest.TestCase):
    def test_moudle(self):
        test_cases = {
            "collection": [
                deque([1, 2, 3]),
                OrderedDict[('a', 1), ('b', 2)],
                defaultdict(int, [('a', 1), ('b', 2)]),
                Counter('safvonusod')],
            "path": Path('./res/test.txt'),
            "datetime": datetime.now(),
            "set":{'a', 1, 3},
            "json":json.dumps({'name': 'Alice', 'age': 12})
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
