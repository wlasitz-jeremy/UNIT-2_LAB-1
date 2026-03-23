# Import OS and CSV Module
import os
import csv

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
        f"6) Exit")



def load_bookings(bookings):
    for day in VALID_DAYS:
        file_name = f"{day}_hotel_booking.csv"
        b = open(file_name, "r")
        content[day] = b.readlines()



def save_bookings(bookings):
    pass



def add_booking():
    pass



def print_day_calender():
    day = input("Day (Monday-Saturday):  ").strip().title()
    file_name = f"{day}_hotel_booking.csv"
    b = open(file_name, "r")
    content = b.readline()
    while content != "":
        items = content.strip().split(",")
        if len(items) < 4:
            content = b.readline()
            continue
        print("{:<15} {:<17} {:<17} {:<17}".format(items[0], items[1], items[2], items[3]))
        content = b.readline()
    b.close()



def find_booking():
    pass



def cancel_booking():
    pass



def change_booking():
    pass








main()
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
