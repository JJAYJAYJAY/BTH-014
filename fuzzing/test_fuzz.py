import hashlib
import platform
import unittest

from fuzzing.generate_data import GenerateData
from lib_pickle import pickle

os_name = platform.system()


class TestFuzz(unittest.TestCase):
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
                    file_name = f"res/{os_name}_test_{i}_write.pkl"
                    with open(file_name, "wb") as f:
                        pickle.dump(val, f)

                    with open(file_name, "rb") as f:
                        self.assertEqual(
                            hashlib.sha256(pickle.dumps(val)).hexdigest(),
                            hashlib.sha256(f.read()).hexdigest()
                        )
                except Exception as e:
                    errors.append((i, e))
        if errors:
            for i, e in errors:
                print(f"Iteration {i} failed: {e}")
            self.fail(f"{len(errors)} iterations failed.")


if __name__ == '__main__':
    unittest.main()
