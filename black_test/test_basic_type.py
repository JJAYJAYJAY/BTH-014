import hashlib
import random
import unittest
import sys
import argparse
import os
import platform
current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
project_root = os.path.dirname(current_dir)

if project_root not in sys.path:
    sys.path.append(project_root)
from tool import utils as t
from lib_pickle import pickle

os_name = platform.system()

class TestBasicType(unittest.TestCase):
    def test_int(self):
        a = 1
        a_pickle1 = pickle.dumps(a)
        a_pickle2 = pickle.dumps(a)
        # t.isFile(args, a, f"res/{os_name}test_int.pkl")
        assert (hashlib.sha256(a_pickle1).hexdigest() == hashlib.sha256(a_pickle2).hexdigest())

    def test_float(self):
        a = 1.0
        a_pickle1 = pickle.dumps(a)
        a_pickle2 = pickle.dumps(a)
        # t.isFile(args, a, f"res/{os_name}test_float.pkl")
        assert (hashlib.sha256(a_pickle1).hexdigest() == hashlib.sha256(a_pickle2).hexdigest())

    def test_high_precision_float(self):
        a = random.uniform(1.0, 1000000000.0)
        a_pickle1 = pickle.dumps(a)
        a_pickle2 = pickle.dumps(a)
        # t.isFile(args, a, f"res/{os_name}test_high_precision_float.pkl")
        assert (hashlib.sha256(a_pickle1).hexdigest() == hashlib.sha256(a_pickle2).hexdigest())

    def test_string(self):
        a = 'hello'
        a_pickle1 = pickle.dumps(a)
        a_pickle2 = pickle.dumps(a)
        # t.isFile(args, a, f"res/{os_name}test_string.pkl")
        assert (hashlib.sha256(a_pickle1).hexdigest() == hashlib.sha256(a_pickle2).hexdigest())

    def test_bytes(self):
        a = b'hello'
        a_pickle1 = pickle.dumps(a)
        a_pickle2 = pickle.dumps(a)
        # t.isFile(args, a, f"res/{os_name}test_bytes.pkl")
        assert (hashlib.sha256(a_pickle1).hexdigest() == hashlib.sha256(a_pickle2).hexdigest())

    def test_none(self):
        a = None
        a_pickle1 = pickle.dumps(a)
        a_pickle2 = pickle.dumps(a)
        # t.isFile(args, a, f"res/{os_name}test_none.pkl")
        assert (hashlib.sha256(a_pickle1).hexdigest() == hashlib.sha256(a_pickle2).hexdigest())

    def test_bool(self):
        a = True
        a_pickle1 = pickle.dumps(a)
        a_pickle2 = pickle.dumps(a)
        # t.isFile(args, a, f"res/{os_name}test_bool.pkl")
        assert (hashlib.sha256(a_pickle1).hexdigest() == hashlib.sha256(a_pickle2).hexdigest())

    def test_bool_write(self):
        a = True
        with open(f"res/{os_name}test_bool_write.pkl", "wb") as f:
            pickle.dump(a, f)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="is file input")
    parser.add_argument("--file", type=int, help="is file input?")
    args = parser.parse_args()
    unittest.main(argv=[sys.argv[0]])
