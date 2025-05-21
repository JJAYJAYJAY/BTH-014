import hashlib
from lib_pickle import pickle
import unittest


class TestContainer(unittest.TestCase):
    def test_list(self):
        a = [1, 'a', 3, 4, 5, 6]
        a_pickle1 = pickle.dumps(a)
        a_pickle2 = pickle.dumps(a)
        assert (hashlib.sha256(a_pickle1).hexdigest() == hashlib.sha256(a_pickle2).hexdigest())

    def test_tuple(self):
        a = (1, 2, '*', 43, '1')
        a_pickle1 = pickle.dumps(a)
        a_pickle2 = pickle.dumps(a)
        assert (hashlib.sha256(a_pickle1).hexdigest() == hashlib.sha256(a_pickle2).hexdigest())

    def test_dict(self):
        a = {'name': 'Alice', 'age': 21}
        a_pickle1 = pickle.dumps(a)
        a_pickle2 = pickle.dumps(a)
        assert (hashlib.sha256(a_pickle1).hexdigest() == hashlib.sha256(a_pickle2).hexdigest())

    def test_set(self):
        a = {'a', 1, 3}
        a_pickle1 = pickle.dumps(a)
        a_pickle2 = pickle.dumps(a)
        assert (hashlib.sha256(a_pickle1).hexdigest() == hashlib.sha256(a_pickle2).hexdigest())

    def test_frozenset(self):
        a = frozenset(['a', 1, 3])
        a_pickle1 = pickle.dumps(a)
        a_pickle2 = pickle.dumps(a)
        assert (hashlib.sha256(a_pickle1).hexdigest() == hashlib.sha256(a_pickle2).hexdigest())


if __name__ == '__main__':
    unittest.main()
