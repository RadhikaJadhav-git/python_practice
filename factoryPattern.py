from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class Razorpay(Payment):
    def pay(self, amount):
        return f"Paid {amount} using Razorpay"


class Stripe(Payment):
    def pay(self, amount):
        return f"Paid {amount} using Stripe"


class PaymentFactory:
    @staticmethod
    def get_payment(method):
        payments = {
            "razorpay": Razorpay,
            "stripe": Stripe,
        }
        if method.lower() not in payments:
            raise ValueError("Invalid Payment Method")
        return payments[method.lower()]()


# Usage
payment = PaymentFactory.get_payment("razorpay")
print(payment.pay(1000))
