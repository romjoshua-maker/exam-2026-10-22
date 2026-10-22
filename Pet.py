from abc import ABC, abstractmethod


class Pet(ABC):
    @abstractmethod
    def get_name(self) -> str:  # getName() in the UML, in Python naming
        pass

    @abstractmethod
    def set_name(self, name: str):  # setName() in the UML
        pass

    @abstractmethod
    def play(self):
        pass
