from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, price):
        pass


class EmailNotifier(Observer):
    def update(self, price):
        print(f"Email sent: Stock price updated to {price}")


class Stock:
    def __init__(self):
        self._observers = []
        self._price = 0

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def set_price(self, price):
        self._price = price
        self.notify()

    def notify(self):
        for observer in self._observers:
            observer.update(self._price)


# Usage
stock = Stock()
stock.attach(EmailNotifier())
stock.set_price(500)
