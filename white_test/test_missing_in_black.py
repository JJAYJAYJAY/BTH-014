import platform
import sys
import unittest

from black_test.Base_test_class import BaseTestClass

py_ver = f"{sys.version_info.major}.{sys.version_info.minor}"

if sys.version_info >= (3, 8):
    from lib_pickle.pickle import PickleBuffer

os_name = platform.system()


class MissingEx:
    def __newobj_ex__(cls, *args, **kwargs):
        return cls.__new__(cls, *args, **kwargs)

    def __reduce_ex__(self, protocol):
        return self.__newobj_ex__, (MissingEx, (), {})


def state_setter(obj, state):
    obj.value = state


class MissingStateSetter:
    def __reduce_ex__(self, protocol):
        return (
            MissingStateSetter,  # func
            (0,),  # args
            42,  # state
            None,  # listitems
            None,  # dictitems
            state_setter
        )


class TestMissing(BaseTestClass):
    def test_missing1(self):
        """line from 583 to 594"""
        test_cases = {
            "missingEx1": MissingEx()
        }

        for name, val in test_cases.items():
            with self.subTest(name=name):
                self.dump_and_check(val, name)

    def test_missing2(self):
        """line from 596 to 599"""
        test_cases = {
            "missingEx2": MissingEx()
        }
        for name, val in test_cases.items():
            with self.subTest(name=name):
                self.dump_and_check(val, name, 3)

    def test_missing3(self):
        """line from 663 to 682"""
        test_cases = {
            "missingState": MissingStateSetter()
        }
        for name, val in test_cases.items():
            with self.subTest(name=name):
                self.dump_and_check(val, name)

    def test_picklebuffer_missing4(self):
        if sys.version_info < (3, 8):
            self.skipTest("PickleBuffer is not available in Python < 3.8")
        """line from 778 to 801"""
        test_cases = {
            "pickleBuffer": PickleBuffer(b"abc")
        }
        for name, val in test_cases.items():
            with self.subTest(name=name):
                self.dump_and_check(val, name, 5)

    def test_str_missing5(self):
        """line from 818 to 823"""
        test_cases = {
            "missingStr": "line1\\line2\nline3\rline4\x1aline5\0end"
        }
        for name, val in test_cases.items():
            with self.subTest(name=name):
                self.dump_and_check(val, name, 0)

    def test_missing5(self):
        """line from 1062 to 1075"""
        test_cases = {
            "FakeData": ...,
        }
        for name, val in test_cases.items():
            with self.subTest(name=name):
                self.dump_and_check(val, name, 2)

    def test_bytearray_missing6(self):
        """line from 763 to 774"""
        test_cases = {
            "bytearray1": bytearray(),
            "bytearray2": bytearray(b"abc"),
        }
        for name, val in test_cases.items():
            with self.subTest(name=name):
                self.dump_and_check(val, name, 4)
        test_cases = {
            "bytearray3": bytearray(b"a" * (64 * 1024)),
            "bytearray4": bytearray(b"xyz"),
        }
        for name, val in test_cases.items():
            with self.subTest(name=name):
                self.dump_and_check(val, name, 5)
if __name__ == '__main__':
    unittest.main()
