class OldPaymentGateway:
    def make_payment(self, amount):
        return f"Old gateway paid {amount}"


class PaymentAdapter:
    def __init__(self, old_gateway):
        self.old_gateway = old_gateway

    def pay(self, amount):
        return self.old_gateway.make_payment(amount)


# Usage
old = OldPaymentGateway()
adapter = PaymentAdapter(old)
print(adapter.pay(500))
