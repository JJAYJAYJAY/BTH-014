import random
import string
import pickle
from generate_basic import generate_random_value

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

if __name__ == "__main__":
    # 生成一个对象
    obj = generate_object()

    # 获取类名
    class_name = obj.__class__.__name__

    # 获取属性
    attributes = vars(obj)

    # 获取方法名
    methods = [func for func in dir(obj) if callable(getattr(obj, func)) and not func.startswith('__')]

    # 输出结果
    print(f"Class Name: {class_name}")
    print(f"Attributes: {attributes}")
    print(f"Methods: {methods}")