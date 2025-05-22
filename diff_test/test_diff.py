import hashlib
import os
import sys
import unittest
from typing import Dict


class BaseCompareClass(unittest.TestCase):
    # 同时支持操作系统和Python版本的路径配置
    _py_ver = f"{sys.version_info.major}.{sys.version_info.minor}"
    _os_paths = {
        "Windows": os.path.join("res", "Windows", _py_ver),
        "Linux": os.path.join("res", "Linux", _py_ver),
        "Darwin": os.path.join("res", "Darwin", _py_ver),
    }

    _py_paths = {
        "py36": os.path.join("res", "Windows", "3.6"),
        "py39": os.path.join("res", "Windows", "3.9"),
        "py311": os.path.join("res", "Windows", "3.11"),
    }

    def compare(self, case_name: str, *, ext: str = "pkl", flag: bool = True) -> None:
        hashes: Dict[str, str] = {}
        result_paths = self._os_paths if flag else self._py_paths
        for platform_key, base_dir in result_paths.items():
            fp = os.path.join(base_dir, f"test_{case_name}_write.{ext}")
            if os.path.exists(fp):
                with open(fp, "rb") as f:
                    hashes[platform_key] = hashlib.sha256(f.read()).hexdigest()

        if len(hashes) < 2:
            self.skipTest(
                f"'{case_name}' only found {len(hashes)} result file(s); skipping comparison"
            )
            return

        ref_platform, ref_hash = next(iter(hashes.items()))
        for platform_key, h in hashes.items():
            self.assertEqual(
                ref_hash,
                h,
                msg=(
                    f"Type '{case_name}' differs between {ref_platform} "
                    f"and {platform_key} result files (Hash: {h[:8]} vs {ref_hash[:8]})"
                ),
            )

    def base_test(self, test_cases: list, flag: bool):
        errors = []
        for name in test_cases:
            with self.subTest(name=name):
                try:
                    self.compare(name, flag=flag)
                except Exception as e:
                    errors.append(f"Different  files for {name}: {e}")
        if errors:
            self.fail("\n".join(errors))


class TestDiffOS(BaseCompareClass):
    def test_basic_type_diff(self):
        test_cases = ["int", "float", "high_float", "str", "byte", "None", "bool"]
        self.base_test(test_cases, flag=True)

    def test_container_diff(self):
        test_cases = ["list", "tuple", "dict", "set", "frozenset"]
        self.base_test(test_cases, flag=True)

    def test_customer_class_diff(self):
        test_cases = ["person", "mathutil", "animal", "bankcount"]
        self.base_test(test_cases, flag=True)

    def test_function_diff(self):
        test_cases = ["function1", "function2", "function3", "function4"]
        self.base_test(test_cases, flag=True)

    def test_module_diff(self):
        test_cases = ["collection", "path", "datetime", "json"]
        self.base_test(test_cases, flag=True)

    def test_nested_diff(self):
        test_cases = ["nested_dict", "nested_class", "nested_list"]
        self.base_test(test_cases, flag=True)

    def test_reference_diff(self):
        test_cases = ["reference"]
        self.base_test(test_cases, flag=True)

    def test_fuzz_diff(self):
        errors = []
        for i in range(100):
            with self.subTest(name=i):
                try:
                    self.compare(f"fuzz{i}")
                except Exception as e:
                    errors.append(f"Different  files for fuzz{i}: {e}")
        if errors:
            self.fail("\n".join(errors))

    def test_white_diff(self):
        test_cases = ["missingEx1", "missingEx2", "missingState", "pickleBuffer", "missingStr", "FakeData"]
        self.base_test(test_cases, flag=True)


class TestDiffPY(BaseCompareClass):
    def test_basic_type_diff(self):
        test_cases = ["int", "float", "high_float", "str", "byte", "None", "bool"]
        self.base_test(test_cases, flag=False)

    def test_container_diff(self):
        test_cases = ["list", "tuple", "dict", "set", "frozenset"]
        self.base_test(test_cases, flag=False)

    def test_customer_class_diff(self):
        test_cases = ["person", "mathutil", "animal", "bankcount"]
        self.base_test(test_cases, flag=False)

    def test_function_diff(self):
        test_cases = ["function1", "function2", "function3", "function4"]
        self.base_test(test_cases, flag=False)

    def test_module_diff(self):
        test_cases = ["collection", "path", "datetime", "json"]
        self.base_test(test_cases, flag=False)

    def test_nested_diff(self):
        test_cases = ["nested_dict", "nested_class", "nested_list"]
        self.base_test(test_cases, flag=False)

    def test_reference_diff(self):
        test_cases = ["reference"]
        self.base_test(test_cases, flag=False)

    def test_fuzz_diff(self):
        errors = []
        for i in range(100):
            with self.subTest(name=i):
                try:
                    self.compare(f"fuzz{i}", flag=False)
                except Exception as e:
                    errors.append(f"Different  files for fuzz{i}: {e}")
        if errors:
            self.fail("\n".join(errors))

    def test_white_diff(self):
        test_cases = ["missingEx1", "missingEx2", "missingState", "pickleBuffer", "missingStr", "FakeData"]
        self.base_test(test_cases, flag=False)
