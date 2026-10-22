from overrides import overrides

from Order import Order


class RegularOrder(Order):
    @overrides
    def calculate_total_price(self) -> float:
        self.total_price = self.get_items_price()  # no discount, even for a VIP customer
        return self.total_price
