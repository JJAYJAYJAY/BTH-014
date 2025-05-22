import sys
import unittest

from black_test.Base_test_class import BaseTestClass


class TestInPoint(unittest.TestCase, BaseTestClass):
    def test_in_point(self):
        # 构建相互引用对象
        a, b = {}, {}
        a["link"] = b
        b["link"] = a

        test_cases = {
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
