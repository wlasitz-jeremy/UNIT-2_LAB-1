bookings = []
flights = []



def view_flights():
    file = open('flights.csv', 'r')
    content = file.readline()
    while content != "":
        content = content.strip().split(",")
        print("{:<15} {:<12} {:<15} {:<17} {:<10}".format(content[0], content[1], content[2], content[3], content[4]))
        content = file.readline()
    file.close()



def book_flights(flights, bookings):
    file = open('flights.csv', 'r')
    content = file.readlines()
    file.close()
    flight_number = input("Enter flight number:\n")
    found = False
    index = 0
    while index < len(content):
        items = content[index].strip().split(",")
        if flight_number == items[0]:
            found = True
            available_seats = int(items[3])
            seats_requested  = int(input("Enter number of seats you want to book:\n"))
            if seats_requested <= available_seats:
                items[3] = str(available_seats - seats_requested)
                content[index] = ",".join(items) + "\n"
                name = input("Enter passenger name:\n")
                booking_string = name + "," + flight_number + "," + str(seats_requested)
                bookings.append(booking_string)
                print("Booking Successful!")
            else:
                print("Sorry, there are no available seats!")
            break
        index += 1
    else:
        print("Flight not found")
    save_flights("flights.csv", content)



def save_flights(file, flights):
    file = open('flights.csv', 'w')
    index = 0
    while index < len(flights):
        file.write(flights[index])
        index += 1
    file.close()



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
    pass



elif choice == '4':
    pass



else:
    exit()
