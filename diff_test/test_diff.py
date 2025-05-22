import hashlib
import itertools
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

    def compare(self, case_name: str, *, ext: str = "pkl", flag: bool = True):
        errors = []
        hashes: Dict[str, str] = {}
        result_paths = self._os_paths if flag else self._py_paths

        # 收集所有平台的哈希值
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
        # 生成所有唯一平台组合

        platforms = list(hashes.keys())
        for a, b in itertools.combinations(platforms, 2):
            with self.subTest(platform_a=a, platform_b=b):
                try:
                    self.assertEqual(
                        hashes[a],
                        hashes[b],
                        msg=(
                            f"Type '{case_name}' differs between {a} "
                            f"and {b} (Hash: {hashes[a][:8]} vs {hashes[b][:8]})"
                        )
                    )
                except Exception as e:
                    errors.append(f"Error comparing {case_name}: {e}")
        return errors

    def base_test(self, test_cases: list, flag: bool):
        errors = []
        for name in test_cases:
            with self.subTest(name=name):
                errors= errors + self.compare(name, flag=flag)

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
        test_cases = ["missingEx1", "missingEx2", "missingState", "pickleBuffer", "missingStr", "FakeData",
                      "bytearray1", "bytearray2", "bytearray3", "bytearray4", ]
        self.base_test(test_cases, flag=True)

    def test_boundary_in_diff(self):
        test_cases = ["simple_list", "simple_dict",
                      "single_char", "nested_list", "nested_dict", "min_unicode",
                      "max_unicode", "float32_min", "reduce_object", "sys_version", "cross_reference"]
        self.base_test(test_cases, flag=True)

    def test_boundary_out_diff(self):
        test_cases = ["lambda", "open_file", "thread_lock", "module"]
        self.base_test(test_cases, flag=True)

    def test_boundary_on_diff(self):
        test_cases = ["empty_list", "empty_dict", "empty_set", "empty_tuple",
                      "zero_int", "zero_float", "zero_complex", "true_value",
                      "false_value", "none_value", "maxsize", "min_int",
                      "infinity", "negative_inf", "nan", "single_element_list",
                      "single_element_dict", "single_element_tuple", "deep_list",
                      "deep_dict", "deep_tuple", "none_type", "object_type",
                      "null_byte", "max_byte"]
        self.base_test(test_cases, flag=True)

    def test_boundary_off_diff(self):
        test_cases = ["deep_list", "deep_dict", "deep_tuple",
                      "huge_float", "path_obj"]
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
        test_cases = ["missingEx1", "missingEx2", "missingState", "pickleBuffer", "missingStr", "FakeData",
                      "bytearray1", "bytearray2", "bytearray3", "bytearray4",]
        self.base_test(test_cases, flag=False)

    def test_boundary_in_diff(self):
        test_cases = ["binint1_max", "binint1_min", "binint2_max", "binint2_min",
                      "protocol_2", "protocol_3", "simple_list", "simple_dict",
                      "single_char", "nested_list", "nested_dict", "min_unicode",
                      "max_unicode", "float32_min", "unit_float", "true_context",
                      "false_context", "reduce_object", "sys_version", "cross_reference"]
        self.base_test(test_cases, flag=False)

    def test_boundary_out_diff(self):
        test_cases = ["lambda", "open_file", "thread_lock", "bad_unicode",
                      "module", "unregistered_class", "timestamp"]
        self.base_test(test_cases, flag=False)

    def test_boundary_on_diff(self):
        test_cases = ["empty_list", "empty_dict", "empty_set", "empty_tuple",
                      "zero_int", "zero_float", "zero_complex", "true_value",
                      "false_value", "none_value", "maxsize", "min_int",
                      "infinity", "negative_inf", "nan", "single_element_list",
                      "single_element_dict", "single_element_tuple", "deep_list",
                      "deep_dict", "deep_tuple", "none_type", "object_type",
                      "null_byte", "max_byte"]
        self.base_test(test_cases, flag=False)

    def test_boundary_off_diff(self):
        test_cases = ["deep_list", "deep_dict", "deep_tuple",
                      "huge_float", "bool_2", "random_obj", "path_obj"]
        self.base_test(test_cases, flag=False)
