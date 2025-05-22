import platform
import unittest

from black_test.Base_test_class import BaseTestClass
from fuzzing.generate_data import GenerateData

os_name = platform.system()


class TestFuzz(unittest.TestCase, BaseTestClass):
    def test_fuzz(self):
        errors = []
        # 读取随机种子
        with open('fuzzing/random_seed.txt', 'r') as f:
            seed = int(f.read().strip())

        # 初始化 GenerateData 类
        data_generator = GenerateData(seed=seed)

        # 生成随机数据并进行测试
        for i in range(100):
            with self.subTest(name=i):
                try:
                    val = data_generator.generate_random_value()
                    self.dump_and_check(val, f"fuzz{i}")
                except Exception as e:
                    errors.append((i, e))
        if errors:
            for i, e in errors:
                print(f"Iteration {i} failed: {e}")
            self.fail(f"{len(errors)} iterations failed.")


if __name__ == '__main__':
    unittest.main()
