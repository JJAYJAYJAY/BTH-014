import json
import pathlib
import platform
import unittest
from collections import Counter, OrderedDict, defaultdict, deque
from datetime import datetime

from black_test.Base_test_class import BaseTestClass

os_name = platform.system()


class TestModule(unittest.TestCase, BaseTestClass):
    def test_module(self):
        test_cases = {
            "collection": [
                deque([1, 2, 3]),
                OrderedDict[('a', 1), ('b', 2)],
                defaultdict(int, [('a', 1), ('b', 2)]),
                Counter('safvonusod')],
            "path": pathlib.Path('/path/to/file'),
            "datetime": datetime.now(),
            "json": json.dumps({'name': 'Alice', 'age': 12})
        }

        for name, val in test_cases.items():
            with self.subTest(name=name):
                self.dump_and_check(val, name)


if __name__ == '__main__':
    unittest.main()
