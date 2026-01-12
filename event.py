class EventRegistration:
    def __init__(self):
        self.users = []

    def register(self, name, email):
        self.users.append({"name": name, "email": email})
        print("Registration successful")

event = EventRegistration()
event.register("Datta", "datta@gmail.com")
print(event.users)
