bookings = []
flights = []



def view_flights():
    f = open('flights.csv', 'r')
    content = f.readline()
    while content != "":
        content = content.strip().split(",")
        print("{:<15} {:<12} {:<15} {:<17} {:<10}".format(content[0], content[1], content[2], content[3], content[4]))
        content = f.readline()
    f.close()



def book_flights(flights, bookings):
    f = open('flights.csv', 'r')
    content = f.readlines()
    f.close()
    b = open("bookings.csv", 'r')
    substance = b.readlines()
    b.close()
    flight_number = input("Enter flight number:\n")
    found = False
    row = 0
    while row < len(content) and row < len(substance):
        items = content[row].strip().split(",")
        if flight_number == items[0]:
            found = True
            available_seats = int(items[3])
            seats_requested  = int(input("Enter number of seats you want to book:\n"))
            if seats_requested <= available_seats:
                items[3] = str(available_seats - seats_requested)
                content[row] = ",".join(items) + "\n"
                name = input("Enter passenger name:\n")
                booking_string = name + "," + flight_number + "," + str(seats_requested)
                substance.append(booking_string + "\n")
                print("Booking Successful!")
            else:
                print("Sorry, there are no available seats!")
            break
        row += 1
    else:
        print("Flight not found")
    save_flights("flights.csv", content)
    save_bookings("bookings.csv", substance)



def save_flights(filename, content):
    f = open(filename, 'w')
    for line in content:
      f.write(line)
    f.close()



def save_bookings(filename, substance):
    b = open(filename, 'w')
    for line in substance:
        b.write(line)
    b.close()



def view_bookings():
    b = open('bookings.csv', 'r')
    substance = b.readline()
    while substance != "":
        substance = substance.strip().split(",")
        print("{:<17} {:<16} {:<17}".format(substance[0], substance[1], substance[2]))
        substance = b.readline()
    b.close()



def cancel_bookings():
    b = open('bookings.csv', 'r')



def main():

    print("Welcome to the Flight Viewer\n"
        "1. View Flights\n"
        "2. Book Flights\n"
        "3. View Bookings\n"
        "4. Cancel Bookings\n"
        "5. Exit"
        )
main()
choice = input("Enter number between 1 and 4:\n")

if choice == '1':
    view_flights()

elif choice == '2':
    book_flights(flights, bookings)

elif choice == '3':
    view_bookings()

elif choice == '4':
    pass



else:
    exit()
