import platform
import unittest

from black_test.Base_test_class import BaseTestClass

os_name = platform.system()


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is{self.name}，I'm {self.age} years old."

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
        raise NotImplementedError("subclass must implement this method")


class Dog(Animal):

    def speak(self):
        return f"{self.name}says:wolf wolf"

    def fetch(self, item: str):
        return f"{self.name}take back {item}"


class Cat(Animal):

    def speak(self):
        return f"{self.name}says:meow meow"

    def knock_over(self, item: str):
        return f"{self.name}knocks over {item}"


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
            raise ValueError("The deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("The withdrawal amount must be positive")
        if amount > self._balance:
            return False
        self._balance -= amount
        return True


class TestCustomerClass(BaseTestClass):
    def test_customer_class(self):
        # TC_003
        test_cases = {
            "person": Person('Alice', 19),
            "mathutil": MathUtils,
            "animal": [Dog('ww'), Cat('mm')],
            "bankcount": BankAccount('Bob', 0),
        }

        for name, val in test_cases.items():
            with self.subTest(name=name):
                self.dump_and_check(val, name)


if __name__ == '__main__':
    unittest.main()
