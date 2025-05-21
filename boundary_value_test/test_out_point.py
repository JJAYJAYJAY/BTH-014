import hashlib
import platform
import random
import threading
import unittest
import sys
from datetime import time

from lib_pickle import pickle
from black_test.Base_test_class import BaseTestClass


class TestOutPoint(unittest.TestCase, BaseTestClass):
    def setUp(self):
        # 创建不可pickle的对象
        self.file = open("temp.txt", "w")
        self.lock = threading.Lock()

    def tearDown(self):
        self.file.close()

    def test_out_point(self):
        test_cases = {
            # 不可序列化对象
            "lambda": lambda x: x,
            "open_file": self.file,
            "thread_lock": self.lock,

            # 非法Unicode
            "bad_unicode": "\ud800",

            # 非法类型
            "module": sys,
            "unregistered_class": self.__class__,

            # 动态对象
            "timestamp": time.time()
        }

        for name, val in test_cases.items():
            with self.subTest(value=name):
                self.dump_and_check(val, name)


if __name__ == '__main__':
    unittest.main()
