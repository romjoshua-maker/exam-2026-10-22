from overrides import overrides

from Animal import Animal
from Pet import Pet

FISH_LEGS = 0


class Fish(Animal, Pet):
    def __init__(self):
        Animal.__init__(self, FISH_LEGS)
        self.__name = ""  # Fish() gets no name - set it with set_name()

    @overrides
    def get_name(self) -> str:
        return self.__name

    @overrides
    def set_name(self, name: str):
        self.__name = name

    @overrides
    def play(self):
        print("Fish swims around the fish tank")

    @overrides
    def walk(self):
        print("Fish can't walk - it has no legs, it swims")

    @overrides
    def eat(self):
        print("Fish eats fish food")
