from overrides import overrides

from CustomerGift import CustomerGift


class Coupon(CustomerGift):
    @overrides
    def open_gift(self):
        print("Congratulations! you got a new gift! Enjoy!")
