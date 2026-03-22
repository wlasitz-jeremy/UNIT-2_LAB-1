bookings = []
flights = []



def view_flights(flights):

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

    flight_number = input("Enter flight number: ")

    found = False
    row = 0

    while row < len(content) and row < len(substance):

        items = content[row].strip().split(",")

        if flight_number == items[0]:

            found = True

            available_seats = int(items[3])
            seats_requested  = int(input("Enter number of seats you want to book: "))

            if seats_requested <= available_seats:
                items[3] = str(available_seats - seats_requested)
                content[row] = ",".join(items) + "\n"

                name = input("Enter passenger name: ")

                booking_string = name + "," + flight_number + "," + str(seats_requested)
                substance.append(booking_string + "\n")
                print("Booking Successful!")
            else:
                print("Sorry, there are no available seats!")
            break

        row += 1
    if not found:
        print("Flight not found")

    save_flights("flights.csv", content)
    save_bookings("bookings.csv", substance)



def save_flights(filename, content):
    f = open(filename, 'w')
    for line in content:
      f.write(line)
    f.close()



def load_flights(filename):
    f = open(filename, 'r')
    content = f.readlines()
    f.close()

    flights_list = []
    row = 0

    while row < len(content):
        items = content[row].strip().split(",")
        flights_list.append(items)
        row += 1
    return flights_list



def save_bookings(filename, substance):
    b = open(filename, 'w')
    for line in substance:
        b.write(line)
    b.close()



def load_bookings(filename):
    b = open(filename, 'r')
    substance = b.readlines()
    b.close()

    bookings_list = []
    row = 0

    while row < len(substance):
        pieces = substance[row].strip().split(",")
        bookings_list.append(pieces)
        row += 1
    return bookings_list



def view_bookings(bookings):

    b = open('bookings.csv', 'r')
    substance = b.readline()

    while substance != "":

        substance = substance.strip().split(",")
        print("{:<17} {:<16} {:<17}".format(substance[0], substance[1], substance[2]))
        substance = b.readline()

    b.close()



def cancel_bookings(flights, bookings):

    b = open("bookings.csv", 'r')
    substance = b.readlines()
    b.close()

    f = open('flights.csv', 'r')
    content = f.readlines()
    f.close()

    flight_number = input("Enter flight number: ")
    name = input("Enter passenger name: ")

    found = False
    b_row = 0

    while b_row < len(substance):

        pieces = substance[b_row].strip().split(",")

        if len(pieces) >= 2 and pieces[1] == flight_number and pieces[0] == name:

            found = True

            substance.pop(b_row)
            f_row = 0

            while f_row < len(content):

                items = content[f_row].strip().split(",")

                if items[0] == flight_number:

                    available_seats = int(items[3])
                    cancelled_seats = int(pieces[2])

                    items[3] = str(available_seats + cancelled_seats)
                    content[f_row] = ",".join(items) + "\n"
                    break

                f_row += 1
            print("Booking Cancelled!")

        b_row += 1
    if not found:
        print("No booking found!")

    save_flights("flights.csv", content)
    save_bookings("bookings.csv", substance)



def main():

    flights = load_flights("flights.csv")
    bookings = load_bookings("bookings.csv")

    print("Welcome to the Flight Viewer\n"
        "1. View Flights\n"
        "2. Book Flights\n"
        "3. View Bookings\n"
        "4. Cancel Bookings\n"
        "5. Exit")

main()
choice = input("Enter number between 1 and 4: ")

while choice != '5':

    if choice == '1':
        view_flights(flights)

    elif choice == '2':
        book_flights(flights, bookings)

    elif choice == '3':
        view_bookings(bookings)

    elif choice == '4':
        cancel_bookings(flights, bookings)

    main()
    choice = input("Enter number between 1 and 4: ")
