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
    bookings = []
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
                line = content[row].strip()
                if "," not in line:
                    row += 1
                    continue
                items = line.split("\t")
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
    room_number = input("Room number (101/102/201): ").strip()
    day = input("Day (Monday-Saturday): ").strip().title()
    file_name = f"{day}_hotel_booking.csv"
    b = open(file_name, "r")
    content = b.readlines()
    b.close()
    hour = input("Hour (9-17): ").strip()
    guest_name = input("Guest name: ").strip().title()
    row = 0
    while row < len(content):
        items = content[row].strip().split("\t")
        if len(items) < 4:
            row += 1
            continue
        if items[0] == "Time":
            row += 1
            continue
        time_value = items[0].split(":")[0].lstrip("0")
        hour = hour.lstrip("0")
        if hour == time_value:
            if room_number == "101":
                room_index = 1
            elif room_number == "102":
                room_index = 2
            elif room_number == "201":
                room_index = 3
            else:
                print("Invalid room number.")
                return
            if items[room_index].lower() != "empty":
                print("Could not add booking.")
                return
            items[room_index] = guest_name
            content[row] = "\t".join(items) + "\n"
            b= open(file_name, "w")
            for line in content:
                b.write(line)
            b.close()
            print("Booking added.")
            return
        row += 1
    print("Invalid hour.")
    save_bookings(bookings)



def print_day_calender():
    day = input("Day (Monday-Saturday): ").strip().title()
    file_name = f"{day}_hotel_booking.csv"
    b = open(file_name, "r")
    content = b.readline()
    header = content.strip().split("\t")
    print("{:<15}".format(header[0]))
    while content != "":
        items = content.strip().split("\t")
        if len(items) < 4:
            content = b.readline()
            continue
        print("{:<15} {:<17} {:<17} {:<17}".format(items[0], items[1], items[2], items[3]))
        content = b.readline()
    b.close()



def find_booking():
    guest_name = input("Guest name: ").strip().title()
    found = False
    for file in os.listdir():
        if file.endswith("_hotel_booking.csv"):
            day = file.split("_")[0]
            b = open(file, "r")
            content = b.readlines()
            while content != "":
                items = content.strip().split("\t")
                if len(items) < 4:
                    if items[1] == guest_name:
                        print(f"{guest_name} is in Room 101 on {day} at {items[1]}")
                        found = True
                    elif items[2] == guest_name:
                        print(f"{guest_name} is in Room 102 on {day} at {items[2]}")
                        found = True
                    elif items[3] == guest_name:
                        print(f"{guest_name} is in Room 201 on {day} at {items[3]}")
                        found = True
                content = b.readline()
            b.close()
    if not found:
        print("No booking found.")



def cancel_booking():
    pass

    save_bookings(bookings)
def change_booking():
    pass

    save_bookings(bookings)



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
        print("Invalid choice, enter 1 to 6")
    option = input("Select option: ").strip()
print ("Saved. Goodbye.")
