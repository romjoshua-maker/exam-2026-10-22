from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, legs: int):
        self._legs = legs  # protected - for Animal and its subclasses

    def walk(self):
        print(f"{type(self).__name__} walks on {self._legs} legs")

    @abstractmethod
    def eat(self):
        pass
