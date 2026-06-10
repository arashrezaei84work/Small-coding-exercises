"""
    This is just an exercise for Maktabkhoone
"""
from abc import ABC, abstractmethod
import secrets


class Father(ABC):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"

    @abstractmethod
    def generate(self):
        pass


class StringPassword(Father):
    def generate(self):
        return ''.join(secrets.choice(self.letters) for _ in range(20))


class IntegerPassword(Father):
    def generate(self):
        return ''.join(secrets.choice(self.numbers) for _ in range(20))


class StrIntPassword(Father):
    def generate(self):
        chars = self.letters + self.numbers
        return ''.join(secrets.choice(chars) for _ in range(20))


ps1 = StringPassword()
print(ps1.generate())
print("=====================")
ps2 = IntegerPassword()
print(ps2.generate())
print("=====================")
ps3 = StrIntPassword()
print(ps3.generate())

