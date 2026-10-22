from CustomerGift import CustomerGift
from CustomerType import CustomerType
from OrderItem import OrderItem

MIN_DISCOUNT = 0
MAX_DISCOUNT = 1


class Customer:
    customer_ids = []  # every customer id in the system - an id can't be used twice

    def __init__(self, id: int, first_name: str, last_name: str, email: str, delivery_address: str,
                 customer_type: CustomerType, favorite_items: list, customer_discount: float = None,
                 customer_gift: CustomerGift = None):
        if id in Customer.customer_ids:
            raise ValueError(f"Customer id {id} already exists")
        if customer_discount is not None and (customer_discount < MIN_DISCOUNT or customer_discount > MAX_DISCOUNT):
            raise ValueError(f"Customer discount must be between {MIN_DISCOUNT} and {MAX_DISCOUNT}")
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.delivery_address = delivery_address
        self.customer_type = customer_type
        self.customer_discount = customer_discount
        self.favorite_items = []
        for item in favorite_items:
            self.add_favorite_item(item)
        self.customer_gift = customer_gift
        Customer.customer_ids.append(self.id)

    def add_favorite_item(self, item: OrderItem):
        for favorite_item in self.favorite_items:
            if favorite_item.item_name == item.item_name:  # same name = same item, even with a different id
                print(f"{item.item_name} is already in {self.first_name}'s favorite items")
                return
        self.favorite_items.append(item)

    def remove_favorite_item(self, item: OrderItem):
        for index, favorite_item in enumerate(self.favorite_items):
            if favorite_item.item_name == item.item_name:
                self.favorite_items.pop(index)  # not remove() - it compares by id
                return
        print(f"{item.item_name} is not in {self.first_name}'s favorite items")

    def take_gift(self, gift: CustomerGift):
        self.customer_gift = gift

    def open_gift(self):
        if self.customer_gift is None:
            print(f"{self.first_name} has no gift to open")
            return
        self.customer_gift.open_gift()

    def __eq__(self, other):
        if not isinstance(other, Customer):
            return NotImplemented
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
