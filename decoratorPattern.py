from abc import ABC, abstractmethod


class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass


class BasicCoffee(Coffee):
    def cost(self):
        return 100


class MilkDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 20


class SugarDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 10


# Usage
coffee = MilkDecorator(SugarDecorator(BasicCoffee()))
print(coffee.cost())  # 130
