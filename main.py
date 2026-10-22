from datetime import datetime

from Animal import Animal
from Cat import Cat
from Coupon import Coupon
from Customer import Customer
from CustomerGift import CustomerGift
from CustomerType import CustomerType
from Fish import Fish
from GiftCard import GiftCard
from Order import Order
from OrderItem import OrderItem
from PaymentType import PaymentType
from Pet import Pet
from RegularOrder import RegularOrder
from Spider import Spider
from VIPOrder import VIPOrder

# ==========================================
# Test Case Output
# ==========================================
if __name__ == '__main__':
    # create order items
    pizza = OrderItem(1, "Pizza", 50)
    cola = OrderItem(2, "Cola", 10)
    salad = OrderItem(3, "Salad", 40)
    print(f"Order item: id {pizza.id}, name {pizza.item_name}, price {pizza.item_price}")

    # create customers - a VIP with a 0.1 (10%) discount, a VIP with no discount (None) and a regular customer
    dana = Customer(1, "Dana", "Levi", "dana@mail.com", "Herzl 1, Tel Aviv", CustomerType.VIP, [], 0.1)
    noa = Customer(2, "Noa", "Bar", "noa@mail.com", "Dizengoff 5, Tel Aviv", CustomerType.VIP,
                   [cola, OrderItem(10, "Cola", 12)])  # same name, different id - added once
    avi = Customer(3, "Avi", "Cohen", "avi@mail.com", "Ben Yehuda 7, Jerusalem", CustomerType.REGULAR, [])
    print(f"Customer: id {dana.id}, {dana.first_name} {dana.last_name}, {dana.email}, {dana.delivery_address}, "
          f"type {dana.customer_type.name}, discount {dana.customer_discount}, gift {dana.customer_gift}")
    print(f"Customer with no discount: {noa.first_name}, discount {noa.customer_discount}")
    try:
        Customer(4, "Ron", "Tal", "ron@mail.com", "Hagana 3, Haifa", CustomerType.VIP, [], 1.5)  # not between 0 and 1
    except ValueError as error:
        print(f"Error: {error}")
    print(f"{noa.first_name}'s favorite items: {[item.item_name for item in noa.favorite_items]}")  # ['Cola']

    # regular order - the sum of the items prices
    regular_order = RegularOrder(1, "Family dinner", avi.delivery_address, [pizza, cola, salad], avi,
                                 PaymentType.CASH, datetime.now())
    print(f"Order: id {regular_order.id}, {regular_order.name}, {regular_order.delivery_address}, "
          f"items {[item.item_name for item in regular_order.items]}, customer {regular_order.customer.first_name}, "
          f"payment {regular_order.payment_type.name}, date {regular_order.order_date}")
    print(f"Regular order total price: {regular_order.total_price:.2f}")  # 50 + 10 + 40 = 100

    # VIP order - the sum with the customer's discount
    vip_order = VIPOrder(2, "Lunch", dana.delivery_address, [pizza, cola], dana, PaymentType.CREDIT_CARD,
                         datetime.now())
    print(f"VIP order total price (discount 0.1): {vip_order.total_price:.2f}")  # 60 - 10% = 54

    # a regular order of a VIP customer - no discount
    dana_regular_order = RegularOrder(3, "Salad", dana.delivery_address, [salad], dana, PaymentType.CHECK,
                                      datetime.now())
    print(f"Regular order of a VIP customer (no discount): {dana_regular_order.total_price:.2f}")  # 40

    # a VIP order of a VIP customer with no discount (None)
    noa_vip_order = VIPOrder(4, "Salad", noa.delivery_address, [salad], noa, PaymentType.OTHER, datetime.now())
    print(f"VIP order of a customer with no discount: {noa_vip_order.total_price:.2f}")  # 40

    # polymorphism - every order calculates its total price its own way
    for order in [regular_order, vip_order, dana_regular_order, noa_vip_order]:
        print(f"{type(order).__name__} {order.id}: {order.calculate_total_price():.2f}")

    # a VIP order of a regular customer - error, and the order's items don't get to the favorites
    steak = OrderItem(4, "Steak", 90)
    try:
        VIPOrder(5, "Party", avi.delivery_address, [steak], avi, PaymentType.CASH, datetime.now())
    except ValueError as error:
        print(f"Error: {error}")
    print(f"{avi.first_name}'s favorite items: {[item.item_name for item in avi.favorite_items]}")  # no Steak

    # item ids are unique - a new item with the pizza's id is an error,
    # and the same item twice in one order is added once
    try:
        OrderItem(1, "Burger", 45)
    except ValueError as error:
        print(f"Error: {error}")
    order_with_same_item = RegularOrder(6, "Dinner", avi.delivery_address, [pizza, pizza, cola], avi,
                                        PaymentType.CASH, datetime.now())
    print(f"Order items: {[item.item_name for item in order_with_same_item.items]}, "
          f"total price: {order_with_same_item.total_price:.2f}")  # Pizza, Cola - 60

    # an order with no items
    empty_order = RegularOrder(7, "Empty", avi.delivery_address, [], avi, PaymentType.CASH, datetime.now())
    print(f"Empty order total price: {empty_order.total_price:.2f}")  # 0

    # order ids and customer ids are unique - a second one with the same id is an error
    try:
        VIPOrder(2, "Copy", dana.delivery_address, [], dana, PaymentType.CASH, datetime.now())
    except ValueError as error:
        print(f"Error: {error}")
    try:
        Customer(1, "Other", "Name", "other@mail.com", "Other 1", CustomerType.REGULAR, [])
    except ValueError as error:
        print(f"Error: {error}")
    print(f"Order ids: {Order.order_ids}, customer ids: {Customer.customer_ids}")  # order 5 failed - not saved
    print(f"Item ids: {OrderItem.item_ids}")
    print(f"Order 2 == order 1: {vip_order == regular_order}, Dana == Avi: {dana == avi}")  # False, False

    # abstract classes can't be created
    try:
        Order(8, "Abstract", avi.delivery_address, [], avi, PaymentType.CASH, datetime.now())
    except TypeError as error:
        print(f"Error: {error}")
    try:
        CustomerGift()
    except TypeError as error:
        print(f"Error: {error}")

    # favorite items - added from the orders automatically, no duplicates by name
    print(f"{avi.first_name}'s favorite items: {[item.item_name for item in avi.favorite_items]}")  # Pizza, Cola, Salad
    avi.add_favorite_item(OrderItem(8, "Pizza", 55))  # same name, different id - already there
    avi.add_favorite_item(OrderItem(9, "Fries", 15))
    avi.remove_favorite_item(salad)
    avi.remove_favorite_item(salad)  # not there anymore
    print(f"{avi.first_name}'s favorite items: {[item.item_name for item in avi.favorite_items]}")  # Pizza, Cola, Fries

    # gifts - a gift can be of any type that has open_gift()
    avi.open_gift()  # no gift yet
    avi.take_gift(GiftCard())
    print(f"{avi.first_name} got a {type(avi.customer_gift).__name__}")
    avi.open_gift()
    dana.take_gift(Coupon())
    print(f"{dana.first_name} got a {type(dana.customer_gift).__name__}")
    dana.open_gift()

    # ==========================================
    # Bonus - Animal / Pet
    # ==========================================
    spider = Spider()
    tom = Cat("Tom")
    cat_without_name = Cat()
    fish = Fish()

    # every animal walks and eats its own way - the fish can't walk
    for animal in [spider, tom, fish]:
        animal.walk()
        animal.eat()

    # the cat and the fish are pets, the spider isn't
    print(f"Is a pet: spider {isinstance(spider, Pet)}, cat {isinstance(tom, Pet)}, fish {isinstance(fish, Pet)}")
    print(f"Cat(name): '{tom.get_name()}', Cat(): '{cat_without_name.get_name()}', Fish(): '{fish.get_name()}'")
    cat_without_name.set_name("Kitty")
    fish.set_name("Nemo")
    print(f"After set_name: '{cat_without_name.get_name()}', '{fish.get_name()}'")
    for pet in [tom, fish]:
        pet.play()

    # Animal and Pet are abstract
    try:
        Animal(4)
    except TypeError as error:
        print(f"Error: {error}")
    try:
        Pet()
    except TypeError as error:
        print(f"Error: {error}")
