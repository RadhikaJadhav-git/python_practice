total_seats = 50
booked_seats = 0

def book_seat(requested):
    global booked_seats
    if booked_seats + requested <= total_seats:
        booked_seats += requested
        print("Booking successful")
    else:
        print("Not enough seats available")

while True:
    seats = int(input("Enter seats to book (0 to exit): "))
    if seats == 0:
        break
    book_seat(seats)
    print("Available seats:", total_seats - booked_seats)
