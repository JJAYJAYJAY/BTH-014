import random
import string


class GenerateData:
    def __init__(self, seed=None):
        self.seed = seed
        random.seed(self.seed)
        if self.seed is not None:
            random.seed(self.seed)

    def generate_char(self):
        return chr(random.randint(32, 0xD7FF))

    def generate_string(self):
        length = random.randint(0, 5)
        return ''.join(self.generate_char() for i in range(length))

    def generate_big_int(self):
        return random.randint(-2 ** 63, 2 ** 63 - 1) ** 100

    def generate_int(self):
        return random.randint(-2 ** 63, 2 ** 63 - 1)

    def generate_float(self):
        choice = random.choice(['normal', 'large', 'small', 'special'])

        if choice == 'normal':
            return random.uniform(-1e3, 1e3)

        elif choice == 'large':
            return random.uniform(1e100, 1e308) * random.choice([-1, 1])

        elif choice == 'small':
            return random.uniform(1e-308, 1e-100) * random.choice([-1, 1])

        elif choice == 'special':
            return random.choice([float('inf'), float('-inf'), float('nan')])

    def generate_b_string(self):
        str = self.generate_string()
        return str.encode()

    def generate_array(self, depth):
        arr = []
        for _ in range(random.randint(1, 5)):
            arr.append(self.generate_random_value(depth + 1))
        return arr

    def generate_dict(self, depth):
        d = {}
        for _ in range(random.randint(1, 5)):
            key = self.generate_string()
            value = self.generate_random_value(depth + 1)
            d[key] = value
        return d

    def generate_deep_array(self):
        a = []
        for i in range(300):
            a = [self.generate_int(), a]
        return a

    def generate_deep_dict(self):
        a = {}
        for i in range(300):
            a = {self.generate_string(): a}
        return a

    def generate_class_name(self):
        return ''.join(random.choices(string.ascii_uppercase, k=5))

    def generate_attribute_name(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits + "_", k=random.randint(3, 8)))

    def generate_method_name(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits + "_", k=random.randint(3, 8)))

    def generate_class(self):
        # 随机生成类的名称
        class_name = self.generate_class_name()

        # 随机生成类的属性名称
        attributes = {f"{self.generate_attribute_name()}": None for _ in range(random.randint(1, 5))}

        # 随机生成类的方法
        methods = {
            f"{self.generate_method_name()}": lambda self: self.generate_random_value()
            for _ in range(random.randint(1, 3))
        }

        class_dict = {**attributes, **methods, '__init__': lambda self: None}

        # 动态创建类
        new_class = type(class_name, (object,), class_dict)

        return new_class

    def generate_object(self):
        generated_class = self.generate_class()  # 动态生成类
        obj = generated_class()

        # 为每个属性赋值
        for attr in generated_class.__dict__:
            if not attr.startswith('__'):  # 忽略内置属性
                value = self.generate_random_value()  # 生成随机值
                setattr(obj, attr, value)  # 绑定到实例
        return obj

    def generate_random_value(self, depth=0):
        options = [
            self.generate_int,
            self.generate_big_int,
            self.generate_string,
            self.generate_float,
            self.generate_b_string,
            self.generate_object,
            lambda: None,
            lambda: True,
            lambda: False
        ]

        if depth <= 3:
            options += [
                lambda: self.generate_array(depth),
                lambda: self.generate_dict(depth)
            ]

        return random.choice(options)()


if __name__ == '__main__':
    generate = GenerateData(100)
    for i in range(100):
        print(generate.generate_random_value())
