import platform
import sys
import unittest

from black_test.Base_test_class import BaseTestClass

os_name = platform.system()


class TestOnPoint(BaseTestClass):
    def test_on_point(self):
        errors = []
        deep_list = []
        deep_dict = {}
        deep_tuple = ()
        for i in range(324):
            deep_list = [deep_list]
            deep_dict = {"1": deep_dict}
            deep_tuple = (deep_tuple)

        test_cases = {
            # 空容器对象
            "empty_list": [],
            "empty_dict": {},
            "empty_set": set(),
            "empty_tuple": (),

            # 数值零
            "zero_int": 0,
            "zero_float": 0.0,
            "zero_complex": 0j,

            # 布尔与None
            "true_value": True,
            "false_value": False,
            "none_value": None,

            # 整数边界
            "maxsize": sys.maxsize,
            "min_int": -sys.maxsize - 1,

            # 特殊浮点数
            "infinity": float('inf'),
            "negative_inf": float('-inf'),
            "nan": float('nan'),

            # 单元素容器
            "single_element_list": [None],
            "single_element_dict": {'key': None},
            "single_element_tuple": (1,),

            # 递归结构
            "deep_list": deep_list,
            "deep_dict": deep_dict,
            "deep_tuple": deep_tuple,

            # 类型对象
            "none_type": type(None),
            "object_type": object,

            # 二进制边界
            "null_byte": b'\x00',
            "max_byte": b'\xff',

        }

        for name, val in test_cases.items():
            with self.subTest(value=name):
                try:
                    self.dump_and_check(val, name)
                except Exception as e:
                    errors.append(f"{e}")
        if errors:
            self.fail('\n'.join(errors))


if __name__ == '__main__':
    unittest.main()
