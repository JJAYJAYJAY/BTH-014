import hashlib
import os
import unittest
import sys


class BaseCompareClass:
    _py_ver = f"{sys.version_info.major}.{sys.version_info.minor}"
    _os_paths = {
        "Windows": os.path.join("res", "Windows", _py_ver),
        "Linux": os.path.join("res", "Linux", _py_ver),
        "Darwin": os.path.join("res", "Darwin", _py_ver),
    }

    def compare(self, case_name: str, *, ext: str = "pkl") -> None:
        hashes: dict[str, str] = {}
        for os_name, base_dir in self._os_paths.items():
            fp = os.path.join(base_dir, f"test_{case_name}_write.{ext}")
            if os.path.exists(fp):
                with open(fp, "rb") as f:
                    hashes[os_name] = hashlib.sha256(f.read()).hexdigest()

        if len(hashes) < 2:
            self.skipTest(
                f"'{case_name}' only found {len(hashes)} result file(s); skipping hash comparison"
            )
            return

        ref_os, ref_hash = next(iter(hashes.items()))
        for os_name, h in hashes.items():
            self.assertEqual(
                ref_hash,
                h,
                msg=f"Type '{case_name}' differs between {ref_os} and {os_name} result files",
            )


class TestDiffOS(unittest.TestCase, BaseCompareClass):
    def test_basic_type_diff(self):
        errors = []
        test_cases = ["int", "float", "high_float", "str", "byte", "None", "bool"]
        for name in test_cases:
            with self.subTest(name=name):
                try:
                    self.compare(name)
                except Exception as e:
                    errors.append(f"Different  files for {name}: {e}")
        if errors:
            self.fail("\n".join(errors))

    def test_container_diff(self):
        errors = []
        test_cases = ["list", "tuple", "dict", "set", "frozenset"]
        for name in test_cases:
            with self.subTest(name=name):
                try:
                    self.compare(name)
                except Exception as e:
                    errors.append(f"Different  files for {name}: {e}")
        if errors:
            self.fail("\n".join(errors))

    def test_customer_class_diff(self):
        errors = []
        test_cases = ["person", "mathutil", "animal", "bankcount"]
        for name in test_cases:
            with self.subTest(name=name):
                try:
                    self.compare(name)
                except Exception as e:
                    errors.append(f"Different  files for {name}: {e}")
        if errors:
            self.fail("\n".join(errors))

    def test_function_diff(self):
        errors = []
        test_cases = ["function1", "function2", "function3", "function4"]
        for name in test_cases:
            with self.subTest(name=name):
                try:
                    self.compare(name)
                except Exception as e:
                    errors.append(f"Different  files for {name}: {e}")
        if errors:
            self.fail("\n".join(errors))

    def test_module_diff(self):
        errors = []
        test_cases = ["collection", "path", "datetime", "json"]
        for name in test_cases:
            with self.subTest(name=name):
                try:
                    self.compare(name)
                except Exception as e:
                    errors.append(f"Different  files for {name}: {e}")
        if errors:
            self.fail("\n".join(errors))

    def test_nested_diff(self):
        errors = []
        test_cases = ["nested_dict", "nested_class", "nested_list"]
        for name in test_cases:
            with self.subTest(name=name):
                try:
                    self.compare(name)
                except Exception as e:
                    errors.append(f"Different  files for {name}: {e}")
        if errors:
            self.fail("\n".join(errors))

    def test_reference_diff(self):
        errors = []
        test_cases = ["reference"]
        for name in test_cases:
            with self.subTest(name=name):
                try:
                    self.compare(name)
                except Exception as e:
                    errors.append(f"Different  files for {name}: {e}")
        if errors:
            self.fail("\n".join(errors))

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


if __name__ == '__main__':
    unittest.main()
