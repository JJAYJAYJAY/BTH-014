import sys
import threading
import unittest
import time

from black_test.Base_test_class import BaseTestClass


class TestOutPoint(BaseTestClass):
    def setUp(self):
        # 创建不可pickle的对象
        self.file = open("temp.txt", "w")
        self.lock = threading.Lock()

    def tearDown(self):
        self.file.close()

    def test_out_point(self):
        errors = []
        
        #TC_011
        test_cases = {
            # # 不可序列化对象
            "lambda": lambda x: x,
            "open_file": self.file,
            "thread_lock": self.lock,

            # 非法类型
            "module": sys,
        }

        for name, val in test_cases.items():
            with self.subTest(value=name):
                try:
                    self.dump_and_check(val, name)
                except Exception as e:
                    errors.append(f"{e}")

        if errors:
            self.fail("\n".join(errors))


if __name__ == '__main__':
    unittest.main()
