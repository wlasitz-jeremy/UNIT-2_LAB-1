# Imports OS module
import os

# Constants
bookings = []
flights = []



def main():
    # Prints welcome message and choices
    print("Welcome to the Flight Viewer\n"
        "1. View Flights\n"
        "2. Book Flights\n"
        "3. View Bookings\n"
        "4. Cancel Bookings\n"
        "5. Exit")
    # Strips all white spaces and converts text to lowercase
    flights_filename = input("Enter the flight data file name: ").strip().lower()
    bookings_filename = input("Enter the booking data file name: ").strip().lower()
    # Loops until file name entered exists
    while not os.path.exists(flights_filename) and not os.path.exists(bookings_filename):
        print(f"Error file {flights_filename} and {bookings_filename }do not exist. Please try again.")
        # Strips all white spaces and converts text to lowercase
        flights_filename = input("Enter the flight data file name: ").strip().lower()
        bookings_filename = input("Enter the booking data file name: ").strip().lower()
    # Saves entered file names in variables
    flights = load_flights(flights_filename)
    bookings = load_bookings(bookings_filename)



def view_flights(flights):
    # Opens file and stores data of file in variable
    f = open("flights.csv", 'r')
    content = f.readline()
    # Loops through content variable
    while content != "":
        # Strips all white spaces as well as splits it via commas
        content = content.strip().split(",")
        # Formats flights file
        print("{:<15} {:<12} {:<15} {:<17} {:<10}".format(content[0], content[1], content[2], content[3], content[4]))
        # Re-stores content in variable
        content = f.readline()
    # Closes the file
    f.close()



def book_flights(flights, bookings):
    # Opens flights file and reads through entire file closing it after
    f = open("flights.csv", 'r')
    content = f.readlines()
    f.close()
    # Opens bookings file and reads through entire file closing it after
    b = open("bookings.csv", 'r')
    substance = b.readlines()
    b.close()
    # Asks user for flight number
    flight_number = input("Enter flight number: ").strip()
    found = False
    row = 0
    # Loops though until end of flights and bookings file
    while row < len(content) and row < len(substance):
        # Splits and strips the current row in both files
        items = content[row].strip().split(",")
        # If the entered flight number exists in the flights file
        if flight_number == items[0]:
            found = True
            # Seats available equals the seats column of the flights file. Enter the amount of seats you wish to book
            available_seats = int(items[3])
            seats_requested  = int(input("Enter number of seats you want to book: ").strip())
            # If the seats you want ot book are less than or equal to the available seats
            if seats_requested <= available_seats:
                # Subtracts seats requested from available seats
                items[3] = str(available_seats - seats_requested)
                # Updates the seats available column in the flights file and adds a new line
                content[row] = ",".join(items) + "\n"
                # Asks for passengers name
                name = input("Enter passenger name: ").strip().title()
                # Updates bookings_string with the passenger name, flight number and amount of seats requested in the proper format
                booking_string = name + "," + flight_number + "," + str(seats_requested)
                # Appends the bookings.csv file with the bookings_string and adds information
                substance.append(booking_string + "\n")
                # Prints booking was created
                print("Booking Successful!")
            else:
                # Prints that there are only {x} amount of seats left available
                print(f"Sorry, there are not enough seats available, only {available_seats} available.")
            break
        # Adds 1 to row so it loops through the next row in the files
        row += 1
    if not found:
        # If flight number is not in flights.csv prints flight not found
        print("Flight not found")
    # Saves information in flights and bookings csv files
    save_flights(flights, content)
    save_bookings(bookings, substance)



def save_flights(flights, content):
    # Opens flights file
    f = open("flights.csv", 'w')
    # Loops through every line in the flights file
    for line in content:
      # Saves the new information in the file
      f.write(line)
    # Closes the file
    f.close()



def load_flights(flights):
    # Opens flights file
    f = open("flights.csv", 'r')
    # Reads entire file
    content = f.readlines()
    # Closes file
    f.close()
    flights_list = []
    row = 0
    # Loops through file until the end
    while row < len(content):
        # strips and splits sections of files
        items = content[row].strip().split(",")
        # Appends items to flights_lists
        flights_list.append(items)
        # Loops through next row
        row += 1
    # Returns flights_list
    return flights_list



def save_bookings(bookings, substance):
    # Opens bookings file
    b = open("bookings.csv", 'w')
    # Loops through every line in the bookings file
    for line in substance:
        # Saves the new information in the file
        b.write(line)
    # Closes the file
    b.close()



def load_bookings(bookings):
    # Opens bookings file
    b = open("bookings.csv", 'r')
    # Reads entire file
    substance = b.readlines()
    # Closes file
    b.close()
    bookings_list = []
    row = 0
    # Loops through until the end
    while row < len(substance):
        # Strips and splits sections of files
        pieces = substance[row].strip().split(",")
        # Appends pieces to booking_list
        bookings_list.append(pieces)
        # Loops through next row
        row += 1
    # Returns bookings_list
    return bookings_list



def view_bookings(bookings):
    # Opens file and stores data of file in variable
    b = open("bookings.csv", 'r')
    substance = b.readline()
    # Loops through substance variable
    while substance != "":
        # Strips all white spaces as well as splits it via commas
        substance = substance.strip().split(",")
        # Formats bookings file
        print("{:<17} {:<16} {:<17}".format(substance[0], substance[1], substance[2]))
        # Re-stores substance in variable
        substance = b.readline()
    # Closes file
    b.close()



def cancel_bookings(flights, bookings):
    # Opens bookings file and reads through entire file closing it after
    b = open("bookings.csv", 'r')
    substance = b.readlines()
    b.close()
    # Opens flights file and reads through entire file closing it after
    f = open("flights.csv", 'r')
    content = f.readlines()
    f.close()
    # Inputs flight number and passenger name
    flight_number = input("Enter flight number: ").strip()
    name = input("Enter passenger name: ").strip().title()
    found = False
    b_row = 0
    # Loops through until end of bookings file
    while b_row < len(substance):
        # Strips and splits current row in bookings file
        pieces = substance[b_row].strip().split(",")
        # If flight number AND name are in bookings file
        if len(pieces) >= 2 and pieces[1] == flight_number and pieces[0] == name:
            found = True
            # If found deletes current row with passenger name AND flight number
            substance.pop(b_row)
            f_row = 0
            # Loops through until end of flights file
            while f_row < len(content):
                # Strips and splits current row in flights file
                items = content[f_row].strip().split(",")
                # Finds corresponding flight number
                if items[0] == flight_number:
                    # Seats available equals the seats column in the flights file
                    available_seats = int(items[3])
                    # Canceled seats equal the booked seats column in the bookings file
                    canceled_seats = int(pieces[2])
                    # Adding canceled seats back into the available seats
                    items[3] = str(available_seats + canceled_seats)
                    # Updates available seats column in flights file and adds a new line
                    content[f_row] = ",".join(items) + "\n"
                    break
                # Loops through next row in flights file
                f_row += 1
            # Prints booking canceled
            print("Booking Canceled!")
        # Loops through next row in bookings file
        b_row += 1
    if not found:
        # # If name and flight number is not in bookings.csv prints booking not found
        print("No booking found!")
    # Saves information flights and bookings csv files
    save_flights(flights, content)
    save_bookings(bookings, substance)

# Runs main function and prompts user input of choice between 1 and 5
main()
choice = input("Enter number between 1 and 5: ").strip()
# Loops through until "5" is selected then exits
while choice != '5':

    if choice == '1':
        view_flights(flights)

    elif choice == '2':
        book_flights(flights, bookings)

    elif choice == '3':
        view_bookings(bookings)

    elif choice == '4':
        cancel_bookings(flights, bookings)

    else:
        print("Invalid choice, please enter number between 1 and 5")
    choice = input("Enter number between 1 and 5: ").strip()
print ("Thank you for using Flight Viewer")
