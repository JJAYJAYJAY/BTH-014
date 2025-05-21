import hashlib
import pathlib
import platform
import random
import threading
import unittest
import sys
from datetime import time

from lib_pickle import pickle
from black_test.Base_test_class import BaseTestClass

class TestOffPoint(unittest.TestCase, BaseTestClass):
    def test_off_point(self):
        deep_list = []
        deep_dict = {}
        deep_tuple = ()
        for i in range(326):
            deep_list = [deep_list]
            deep_dict = {"1": deep_dict}
            deep_tuple = (deep_tuple)

        test_cases = {
            # 超出递归结构
            "deep_list": deep_list,
            "deep_dict": deep_dict,
            "deep_tuple": deep_tuple,

            # 浮点溢出
            "huge_float": 1e3009,

            # 类型转换
            "bool_2": bool(2),

            # 动态状态对象
            "random_obj": random.Random(),

            # 路径对象
            "path_obj": pathlib.Path('/path/to/file')
        }

        for name, val in test_cases.items():
            with self.subTest(value=name):
                self.dump_and_check(val, name)


if __name__ == '__main__':
    unittest.main()
