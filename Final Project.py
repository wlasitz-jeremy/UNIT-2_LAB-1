# Import OS Module
import csv
import os

# Constants
VALID_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
VALID_HOURS = 9-17
ROOMS = (101, 102, 201)
bookings = []
content = {}


def main():

    print(f"Simple Hotel Booking\n"
        f"1) Add booking\n"
        f"2) Show day calender\n"
        f"3) Find booking by guest\n"
        f"4) Cancel booking\n"
        f"5) Change booking\n"
        f"6) Exit\n")
    # Strips all white spaces and converts text to lowercase
    bookings_filename = input("Enter the booking data file name: ").strip().lower()
    # Loops until file name entered exists
    while not os.path.exists(bookings_filename):
        print(f"Error file {bookings_filename} does not exist. Please enter a valid file name.")
        # Strips all white spaces and converts text to lowercase
        bookings_filename = input("Enter the booking data file name: ").strip().lower()
    # Saves entered file names in variable
    bookings = load_bookings(bookings_filename)

def load_bookings(bookings):
    for day in VALID_DAYS:
        file_name = f"{day}_hotel_booking.csv"
        b = open(file_name, "r")
        content[day] = b.readlines()


















def save_bookings(bookings):




def add_booking():


def print_day_calender():


def find_booking():


def cancel_booking():


def change_booking():










option = input("Select option: ")

while option != '6':

    if option == '1':
        add_booking()

    elif option == '2':
        print_day_calender()

    elif option == '3':
       find_booking()

    elif option == '4':
        cancel_booking()

    elif option == '5':
        change_booking()

    else:
        print("Invalid choice, please enter number between 1 and 6")
    option = input("Enter number between 1 and 5: ").strip()
print ("Saved. Goodbye.")
