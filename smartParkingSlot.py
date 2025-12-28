total_slots = 10
occupied = []

while True:
    choice = input("Park / Exit / Status / Stop: ").lower()

    if choice == "park":
        if len(occupied) < total_slots:
            car = input("Enter car number: ")
            occupied.append(car)
            print("Car parked")
        else:
            print("Parking Full")

    elif choice == "exit":
        car = input("Enter car number: ")
        if car in occupied:
            occupied.remove(car)
            print("Car exited")
        else:
            print("Car not found")

    elif choice == "status":
        print("Available slots:", total_slots - len(occupied))
        print("Parked cars:", occupied)

    elif choice == "stop":
        break
