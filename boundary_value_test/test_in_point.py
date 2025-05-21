import hashlib
import platform
import random
import unittest
import sys

from lib_pickle import pickle
from black_test.Base_test_class import BaseTestClass

class TestInPoint(unittest.TestCase, BaseTestClass):
    def test_in_point(self):
        # 构建相互引用对象
        a, b = {}, {}
        a["link"] = b
        b["link"] = a

        test_cases = {
            # 整数存储边界
            "binint1_max": 127,
            "binint1_min": -128,
            "binint2_max": 32767,
            "binint2_min": -32768,

            # 有效协议版本
            "protocol_2": 2,
            "protocol_3": 3,

            # 有效数据结构
            "simple_list": [1],
            "simple_dict": {"a": 1},
            "single_char": "a",

            # 正常嵌套结构
            "nested_list": [[1]],
            "nested_dict": {"a": {"b": 2}},

            # Unicode边界
            "min_unicode": "\u0000",
            "max_unicode": "\U0010ffff",

            # 浮点精度
            "float32_min": 1.17549435e-38,
            "unit_float": 1.0,

            # 布尔上下文
            "true_context": 1,
            "false_context": 0,

            # 自定义对象
            "reduce_object": self._create_reduce_obj(),

            # 模块属性
            "sys_version": sys.version,

            # 交叉引用
            "cross_reference": a
        }

        for name, val in test_cases.items():
            with self.subTest(value=name):
                self.dump_and_check(val, name)

    def _create_reduce_obj(self):
        # 创建实现__reduce__的自定义对象
        class CustomReduce:
            def __reduce__(self):
                return (str, ("reduced",))
        return CustomReduce()

if __name__ == '__main__':
    unittest.main()
