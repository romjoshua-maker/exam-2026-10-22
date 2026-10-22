from overrides import overrides

from CustomerType import CustomerType
from Order import Order


class VIPOrder(Order):
    @overrides
    def calculate_total_price(self) -> float:
        if self.customer.customer_type != CustomerType.VIP:
            raise ValueError(f"{self.customer.first_name} is not a VIP customer - can't make a VIP order")
        discount = self.customer.customer_discount
        if discount is None:  # a VIP customer without a discount
            discount = 0
        self.total_price = self.get_items_price() * (1 - discount)  # discount 0.05 = 5%
        return self.total_price
