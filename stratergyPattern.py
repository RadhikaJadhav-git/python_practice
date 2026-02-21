from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, amount):
        pass


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent):
        self.percent = percent

    def apply_discount(self, amount):
        return amount - (amount * self.percent / 100)


class FlatDiscount(DiscountStrategy):
    def __init__(self, flat_amount):
        self.flat_amount = flat_amount

    def apply_discount(self, amount):
        return amount - self.flat_amount


class ShoppingCart:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy

    def checkout(self, amount):
        return self.discount_strategy.apply_discount(amount)


# Usage
cart = ShoppingCart(PercentageDiscount(10))
print(cart.checkout(1000))
