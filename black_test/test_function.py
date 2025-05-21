import hashlib
from lib_pickle import pickle
import unittest


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
    def test_function1(self):
        a = function1
        a_pickle1 = pickle.dumps(a)
        a_pickle2 = pickle.dumps(a)
        assert (hashlib.sha256(a_pickle1).hexdigest() == hashlib.sha256(a_pickle2).hexdigest())

    def test_function2(self):
        a = function2
        a_pickle1 = pickle.dumps(a)
        a_pickle2 = pickle.dumps(a)
        assert (hashlib.sha256(a_pickle1).hexdigest() == hashlib.sha256(a_pickle2).hexdigest())

    def test_function3(self):
        a = function3
        a_pickle1 = pickle.dumps(a)
        a_pickle2 = pickle.dumps(a)
        assert (hashlib.sha256(a_pickle1).hexdigest() == hashlib.sha256(a_pickle2).hexdigest())

    def test_function4(self):
        a = function4
        a_pickle1 = pickle.dumps(a)
        a_pickle2 = pickle.dumps(a)
        assert (hashlib.sha256(a_pickle1).hexdigest() == hashlib.sha256(a_pickle2).hexdigest())


if __name__ == '__main__':
    unittest.main()
