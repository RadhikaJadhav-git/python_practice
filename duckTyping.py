class Laptop:
    def work(self):
        print("Coding...")

class Mobile:
    def work(self):
        print("Calling...")

def device_use(device):
    device.work()

device_use(Mobile())
device_use(Laptop())
