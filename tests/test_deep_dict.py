import pickle

class TestClass:
    def __init__(self, name, age, data):
        self.name = name
        self.age = age
        self.data = data

    def add_data(self, new_data):
        """用于修改对象的数据"""
        self.data.append(new_data)

a = []
for i in range(256):
    a = [a]
b = [a]

# 创建 TestClass 的一个实例
obj1 = TestClass("John Doe", a, [1, 2, 3])
obj2 = TestClass("John Doe", b, [1, 2, 3])

b1 = pickle.dumps(obj1)

b2 = pickle.dumps(obj2)

print(b1 == b2)