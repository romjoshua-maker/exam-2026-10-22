from overrides import overrides

from Animal import Animal

SPIDER_LEGS = 8


class Spider(Animal):
    def __init__(self):
        super().__init__(SPIDER_LEGS)

    @overrides
    def eat(self):
        print("Spider eats insects")
