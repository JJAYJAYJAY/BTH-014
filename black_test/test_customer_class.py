import hashlib
import pickle
import unittest

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"你好，我叫{self.name}，今年{self.age}岁。"
    
    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"
    
    def __repr__(self):
        return f"Person(name={repr(self.name)}, age={self.age})"

class MathUtils:
    
    PI = 3.1415926
    
    @classmethod
    def circle_area(cls, radius: float):
        return cls.PI * radius ** 2
    
    @staticmethod
    def is_even(num: int):
        return num % 2 == 0
    
    @classmethod
    def set_pi_precision(cls, digits: int):
        cls.PI = round(3.141592653589793, digits)

class Animal:
    
    def __init__(self, name: str):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("子类必须实现此方法")

class Dog(Animal):
    
    def speak(self):
        return f"{self.name}说：汪汪！"
    
    def fetch(self, item: str):
        return f"{self.name}叼回了{item}"

class Cat(Animal):
    
    def speak(self):
        return f"{self.name}说：喵喵"
    
    def knock_over(self, item: str):
        return f"{self.name}把{item}扑倒了"

class BankAccount:
    
    def __init__(self, owner: str, initial_balance: float = 0):
        self._owner = owner
        self._balance = initial_balance
    
    @property
    def owner(self):
        return self._owner
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("存款金额必须为正数")
        self._balance += amount
    
    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("取款金额必须为正数")
        if amount > self._balance:
            return False
        self._balance -= amount
        return True
    
class TestCustomerClass(unittest.TestCase):
    def test_person(self):
        a = Person('Alice',19)
        a_pickle1 = pickle.dumps(a)
        a_pickle2 = pickle.dumps(a)
        assert (hashlib.sha256(a_pickle1).hexdigest() == hashlib.sha256(a_pickle2).hexdigest())

    def test_mathutils(self):
        a = MathUtils
        a_pickle1 = pickle.dumps(a)
        a_pickle2 = pickle.dumps(a)
        assert (hashlib.sha256(a_pickle1).hexdigest() == hashlib.sha256(a_pickle2).hexdigest())

    def test_Animal(self):
        a = [Dog('ww'),Cat('mm')]
        a_pickle1 = pickle.dumps(a)
        a_pickle2 = pickle.dumps(a)
        assert (hashlib.sha256(a_pickle1).hexdigest() == hashlib.sha256(a_pickle2).hexdigest())

    def test_bankaccount(self):
        a = BankAccount('Mint',0)
        a_pickle1 = pickle.dumps(a)
        a_pickle2 = pickle.dumps(a)
        assert (hashlib.sha256(a_pickle1).hexdigest() == hashlib.sha256(a_pickle2).hexdigest())
        
if __name__ == '__main__':
    unittest.main()
    
