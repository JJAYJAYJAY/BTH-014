import hashlib
import random
import string
import unittest

from generate_basic import generate_random_value
from lib_pickle import pickle


def generate_class_name():
    return ''.join(random.choices(string.ascii_uppercase, k=5))


def generate_attribute_name():
    return ''.join(random.choices(string.ascii_lowercase + string.digits + "_", k=random.randint(3, 8)))


def generate_method_name():
    return ''.join(random.choices(string.ascii_lowercase + string.digits + "_", k=random.randint(3, 8)))


def generate_class():
    # 随机生成类的名称
    class_name = generate_class_name()

    # 随机生成类的属性和方法
    attributes = {f"{generate_attribute_name()}": generate_random_value() for i in range(random.randint(1, 5))}
    methods = {
        f"{generate_method_name()}": lambda self: generate_random_value()
        for i in range(random.randint(1, 3))
    }

    print(attributes)

    class_dict = {**attributes, **methods, '__init__': lambda self: None}

    # 动态创建类
    new_class = type(class_name, (object,), class_dict)

    return new_class


def generate_object():
    generated_class = generate_class()
    obj = generated_class()
    for attr, value in generated_class.__dict__.items():
        if not attr.startswith('__'):  # 忽略内置属性
            setattr(obj, attr, value)  # 绑定到实例
    return obj


class TestGenerateClass(unittest.TestCase):
    def test_generate_class(self):
        for _ in range(10):
            obj = generate_object()
            a_s1 = pickle.dumps(obj)
            a_s2 = pickle.dumps(obj)
            assert (hashlib.sha256(a_s1).hexdigest() == hashlib.sha256(a_s2).hexdigest())
