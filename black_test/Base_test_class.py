import hashlib
import os
import platform
import sys

from lib_pickle import pickle


class BaseTestClass:
    def dump_and_check(self, value, case_name):
        os_name = platform.system()  # Windows / Linux / Darwin
        py_ver = f"{sys.version_info.major}.{sys.version_info.minor}"
        dir_path = os.path.join("res", os_name, py_ver)
        os.makedirs(dir_path, exist_ok=True)  # 幂等

        file_path = os.path.join(dir_path, f"test_{case_name}_write.pkl")

        # 序列化
        with open(file_path, "wb") as f:
            pickle.dump(value, f)

        # 反序列化并比对哈希
        with open(file_path, "rb") as f:
            self.assertEqual(
                hashlib.sha256(pickle.dumps(value)).hexdigest(),
                hashlib.sha256(f.read()).hexdigest(),
                msg=f"SHA256 mismatch for case '{case_name}'"
            )
