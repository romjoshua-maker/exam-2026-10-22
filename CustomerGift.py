from abc import ABC, abstractmethod


class CustomerGift(ABC):
    @abstractmethod
    def open_gift(self):
        pass
