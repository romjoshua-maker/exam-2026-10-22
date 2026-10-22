from abc import ABC, abstractmethod
from datetime import datetime

from Customer import Customer
from PaymentType import PaymentType


class Order(ABC):
    order_ids = []  # every order id in the system - an id can't be used twice

    def __init__(self, id: int, name: str, delivery_address: str, items: list, customer: Customer,
                 payment_type: PaymentType, order_date: datetime):
        if id in Order.order_ids:
            raise ValueError(f"Order id {id} already exists")
        self.id = id
        self.name = name
        self.delivery_address = delivery_address
        self.items = []
        for item in items:
            if item in self.items:  # item ids are unique in an order
                print(f"Item id {item.id} is already in order {self.id} - {item.item_name} was not added")
                continue
            self.items.append(item)
        self.customer = customer
        self.payment_type = payment_type
        self.order_date = order_date
        self.total_price = self.calculate_total_price()
        Order.order_ids.append(self.id)  # only after the VIP check passed
        for item in self.items:  # after the price - a VIP order that failed doesn't change the favorites
            customer.add_favorite_item(item)

    def get_items_price(self) -> float:
        items_price = 0
        for item in self.items:
            items_price += item.item_price
        return items_price

    @abstractmethod
    def calculate_total_price(self) -> float:
        pass

    def __eq__(self, other):
        if not isinstance(other, Order):
            return NotImplemented
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
