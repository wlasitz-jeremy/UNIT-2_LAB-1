# Import OS and CSV Module
import os
import csv


# Constants
VALID_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
VALID_HOURS = range (9, 18)
ROOMS = (101, 102, 201)
bookings = []
content = {}
day = ""
file_name = ""



def normalize_day():
    pass



def slot_key():
    pass



def main():
    bookings = []
    print(f"Simple Hotel Booking\n"
        f"1) Add booking\n"
        f"2) Show day calender\n"
        f"3) Find booking by guest\n"
        f"4) Cancel booking\n"
        f"5) Change booking\n"
        f"6) Exit")
    bookings = load_bookings(file_name)



def load_bookings(file_name):
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



def save_bookings(file_name, bookings):
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
    save_bookings(file_name, bookings)



def print_day_calender(bookings, day):
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
            row = 1
            while row < len(content):
                items = content[row].strip().split("\t")
                time = items[0]
                if items[1].title() == guest_name:
                    print(f"{guest_name} is in Room 101 on {day.title()} at {items[0]}")
                    found = True
                elif items[2].title() == guest_name:
                    print(f"{guest_name} is in Room 102 on {day.title()} at {items[0]}")
                    found = True
                elif items[3].title() == guest_name:
                    print(f"{guest_name} is in Room 201 on {day.title()} at {items[0]}")
                    found = True
                row += 1
            b.close()
    if not found:
        print("No booking found.")



def cancel_booking():
    room_number = input("Room number: ").strip()
    day = input("Day: ").strip().title()
    file_name = f"{day}_hotel_booking.csv"
    b = open(file_name, "r")
    content = b.readlines()
    b.close()
    hour = input("Hour: ").strip()
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
            if items[room_index].lower() == "empty":
                print("No booking found.")
                return
            items[room_index] = "empty"
            content[row] = "\t".join(items) + "\n"
            b = open(file_name, "w")
            for line in content:
                b.write(line)
            b.close()
            print("Canceled.")
            return
        row += 1
    print("Invalid hour.")
    save_bookings(file_name, bookings)



def change_booking():
    guest_name = input("Guest name: ").strip().title()
    found = False
    old_file = ""
    old_row = -1
    old_column = -1
    for file in os.listdir():
        if file.endswith("_hotel_booking.csv"):
            b = open(file, "r")
            content = b.readlines()
            b.close()
            row = 0
            while row < len(content):
                items = content[row].strip().split("\t")
                if len(items) >= 4:
                    if items[1].title() == guest_name:
                        found = True
                        old_file = file
                        old_row = row
                        old_column = 1
                    elif items[2].title() == guest_name:
                        found = True
                        old_file = file
                        old_row = row
                        old_column = 2
                    elif items[3].title() == guest_name:
                        found = True
                        old_file = file
                        old_row = row
                        old_column = 3
                row += 1
    if not found:
        print("No booking found.")
        return
    b = open(old_file, "r")
    old_content = b.readlines()
    b.close()

    old_items = old_content[old_row].strip().split("\t")
    old_items[old_column] = "empty"
    old_content[old_row] = "\t".join(old_items) + "\n"

    b = open(old_file, "w")
    for line in old_content:
        b.write(line)
    b.close()
    room_number = input("New room: ").strip()
    day = input("New day: ").strip().title()
    file_name = f"{day}_hotel_booking.csv"
    b = open(file_name, "r")
    content = b.readlines()
    b.close()
    hour = input("New hour: ").strip()
    hour = hour.lstrip("0")
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
            b = open(file_name, "w")
            for line in content:
                b.write(line)
            b.close()
            print("Booking changed.")
            return
        row += 1
    print("Invalid hour.")
    save_bookings(file_name, bookings)



main()
option = input("Select option: ").strip()

while option != '6':

    if option == '1':
        add_booking(bookings)

    elif option == '2':
        print_day_calender(bookings, day)

    elif option == '3':
       find_booking()

    elif option == '4':
        cancel_booking()

    elif option == '5':
        change_booking()

    else:
        print("Invalid choice, enter 1 to 6")
    main()
    option = input("Select option: ").strip()
print ("Saved. Goodbye.")
