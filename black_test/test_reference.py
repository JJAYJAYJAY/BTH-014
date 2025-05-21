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
        a = generator()
        a_pickle1 = pickle.dumps(a)
        a_pickle2 = pickle.dumps(a)
        assert (hashlib.sha256(a_pickle1).hexdigest() == hashlib.sha256(a_pickle2).hexdigest())


if __name__ == '__main__':
    unittest.main()
