import pathlib
import random
import unittest

from black_test.Base_test_class import BaseTestClass


class TestOffPoint(BaseTestClass):
    def test_off_point(self):
        errors = []
        deep_list = []
        deep_dict = {}
        deep_tuple = ()
        for i in range(325):
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

            # 路径对象
            "path_obj": pathlib.Path('/path/to/file')
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
