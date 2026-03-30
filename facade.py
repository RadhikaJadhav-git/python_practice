class Inventory:
    def check(self):
        return "Inventory checked"


class PaymentService:
    def process(self):
        return "Payment processed"


class Shipping:
    def ship(self):
        return "Item shipped"


class OrderFacade:
    def place_order(self):
        inventory = Inventory()
        payment = PaymentService()
        shipping = Shipping()

        print(inventory.check())
        print(payment.process())
        print(shipping.ship())


# Usage
order = OrderFacade()
order.place_order()
