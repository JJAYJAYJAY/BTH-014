import hashlib
import json
import unittest
from collections import Counter, OrderedDict, defaultdict, deque, namedtuple
from datetime import datetime
from pathlib import Path

from lib_pickle import pickle


class TestMoudle(unittest.TestCase):
    def test_collections(self):
        a = [
            deque([1, 2, 3]),
            OrderedDict[('a', 1), ('b', 2)],
            defaultdict(int, [('a', 1), ('b', 2)]),
            Counter('safvonusod'),
            namedtuple('Point', ['x', 'y'])  # 这个会报错
        ]
        a_pickle1 = pickle.dumps(a)
        a_pickle2 = pickle.dumps(a)
        assert (hashlib.sha256(a_pickle1).hexdigest() == hashlib.sha256(a_pickle2).hexdigest())

    def test_path(self):
        a = Path('./res/test.txt')
        a_pickle1 = pickle.dumps(a)
        a_pickle2 = pickle.dumps(a)
        assert (hashlib.sha256(a_pickle1).hexdigest() == hashlib.sha256(a_pickle2).hexdigest())

    def test_datatime(self):
        a = datetime.now()
        a_pickle1 = pickle.dumps(a)
        a_pickle2 = pickle.dumps(a)
        assert (hashlib.sha256(a_pickle1).hexdigest() == hashlib.sha256(a_pickle2).hexdigest())

    def test_json(self):
        a = json.dumps({'name': 'Alice', 'age': 12})
        a_pickle1 = pickle.dumps(a)
        a_pickle2 = pickle.dumps(a)
        assert (hashlib.sha256(a_pickle1).hexdigest() == hashlib.sha256(a_pickle2).hexdigest())


if __name__ == '__main__':
    unittest.main()
