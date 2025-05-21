import hashlib
import platform
import random
import sys
import unittest
from generate_data import GenerateData

from lib_pickle import pickle

os_name = platform.system()

class TestFuzz(unittest.TestCase):
    def test_fuzz(self):
        # 读取随机种子
        with open('random_seed.txt', 'r') as f:
            seed = int(f.read().strip())

        # 初始化 GenerateData 类
        data_generator = GenerateData(seed=seed)

        # 生成随机数据并进行测试
        for i in range(100):
            # 生成随机数据
            val = data_generator.generate_random_value()

            # 将生成的数据序列化并写入文件
            file_name = f"res/{os_name}_test_{i}_write.pkl"
            with open(file_name, "wb") as f:
                pickle.dump(val, f)

            # 重新打开文件，反序列化并进行哈希对比
            with open(file_name, "rb") as f:
                self.assertEqual(
                    hashlib.sha256(pickle.dumps(val)).hexdigest(),
                    hashlib.sha256(f.read()).hexdigest()
                )


if __name__ == '__main__':
    unittest.main()
