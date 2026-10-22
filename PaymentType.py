from enum import Enum


class PaymentType(Enum):
    CREDIT_CARD = 1
    CASH = 2
    CHECK = 3
    OTHER = 4
