from overrides import overrides

from Animal import Animal
from Pet import Pet

CAT_LEGS = 4


class Cat(Animal, Pet):
    def __init__(self, name: str = ""):  # Cat(name) and Cat() in one constructor
        Animal.__init__(self, CAT_LEGS)
        self.__name = name

    @overrides
    def get_name(self) -> str:
        return self.__name

    @overrides
    def set_name(self, name: str):
        self.__name = name

    @overrides
    def play(self):
        print("Cat plays with a ball of yarn")

    @overrides
    def eat(self):
        print("Cat eats cat food")
