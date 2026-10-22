class OrderItem:
    item_ids = []  # every item id in the system - an id can't be used twice

    def __init__(self, id: int, item_name: str, item_price: float):
        if id in OrderItem.item_ids:
            raise ValueError(f"Item id {id} already exists")
        self.id = id
        self.item_name = item_name
        self.item_price = item_price
        OrderItem.item_ids.append(self.id)

    def __eq__(self, other):
        if not isinstance(other, OrderItem):
            return NotImplemented
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
