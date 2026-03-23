# Import OS and CSV Module
import os
import csv

# Constants
VALID_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
VALID_HOURS = (9, 18)
ROOMS = (101, 102, 201)
bookings = []
content = {}



def main():
    global bookings


    print(f"Simple Hotel Booking\n"
        f"1) Add booking\n"
        f"2) Show day calender\n"
        f"3) Find booking by guest\n"
        f"4) Cancel booking\n"
        f"5) Change booking\n"
        f"6) Exit")

    bookings = load_bookings(bookings)



def load_bookings(bookings):
    bookings = []
    for file in os.listdir():
        if file.endswith("_hotel_booking.csv"):
            b = open(file, "r")
            content = b.readlines()
            b.close()
            row = 0
            while row < len(content):
                items = content[row].strip().split(",")
                bookings.append(items)
                row += 1
    return bookings



def save_bookings(bookings):
    days = {}
    row = 0
    while row < len(bookings):
        items = bookings[row]
        if len(items) < 4:
            row += 1
            continue
        day= items[0].title()
        if day not in days:
            days[day] = []
        days[day].append(items)
        row += 1
        for day in days:
            file_name = f"{day}_hotel_booking.csv"
            b = open(file_name, "w")
            b.write("Day,Room,Hour,Guest\n")
            rows = days[day]
            r = 0
            while r < len(rows):
                line = ",".join(rows[r])
                b.write(line + "\n")
                r += 1
            b.close()



def add_booking(bookings):

    room_number = input("Room number (101/102/201): ")
    day = input("Day (Monday-Saturday): ").strip().title()
    file_name = f"{day}_hotel_booking.csv"
    b = open(file_name, "r")
    content = b.readlines()
    b.close()
    hour = input("Hour (9-17): ").strip()
    guest_name = input("Guest name: ").strip().title()
    row =0
    while row < len(content):
        items = content[row].strip().split(",")
        if len(items) < 4:
            row += 1
            continue
        if room_number == items[1] or items[2] or items[3]:
            if hour in VALID_HOURS:




def print_day_calender():
    day = input("Day (Monday-Saturday): ").strip().title()
    file_name = f"{day}_hotel_booking.csv"
    b = open(file_name, "r")
    content = b.readline()
    header = content.strip().split(",")
    print("{:<15}".format(header[0]))
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
option = input("Select option: ").strip()

while option != '6':

    if option == '1':
        add_booking(bookings)

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
    option = input("Select option: ").strip()
print ("Saved. Goodbye.")
