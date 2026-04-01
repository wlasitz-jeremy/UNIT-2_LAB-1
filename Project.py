import os

VALID_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
VALID_HOURS = range(9, 18)
ROOMS = [101, 102, 201]
FILE_NAME = "hotel_bookings.csv"


class HotelBookingSystem:


    def __init__(self):
        self.bookings = []
        self.load_bookings(FILE_NAME)


    def __str__(self):
        # if csv file doesn't exist prints no loaded bookings
        if not self.bookings:
            return "Hotel Booking System (no bookings loaded)."
        # formats csv file properly
        lines = ["Day,Room,Hour,Guest"]
        for b in self.bookings:
            lines.append(
                f"{b['Day']},{b['Room']},{b['Hour']},{b['Guest']}"
            )
        return "\n".join(lines)


    @staticmethod
    def normalize_day(day):
        # removes white spaces and converts to title case
        return day.strip().title()


    def slot_key(self, day, room, hour):
        # standardizes the file format
        day = self.normalize_day(day)
        return day, room, hour


    def load_bookings(self, FILE_NAME):
        # creates the file if it does not exist
        if not os.path.exists(FILE_NAME):
            return
        # opens file, reads it then closes it
        b = open(FILE_NAME, "r")
        content = b.readlines()
        b.close()
        # skips the heading and strips and splits each row
        for row in content:
            if row.strip() == "":
                continue
            day, room, hour, guest = row.strip().split(",")
            if day == "Day":
                continue
            # appends the information to the file
            self.bookings.append({
                "Day": day,
                "Room": int(room),
                "Hour": int(hour),
                "Guest": guest})


    def save_bookings(self):
        # opens file and writes the information into the file
        b = open(FILE_NAME, "w")
        b.write("Day,Room,Hour,Guest\n")
        # writes the information into the file in the correct format adding a new line before closing it
        for booking in self.bookings:
            line = f"{booking['Day']},{booking['Room']},{booking['Hour']},{booking['Guest']}"
            b.write(line + "\n")
        b.close()
        print("Saved. Goodbye.")


    def add_booking(self):
        # gets input for the room number, day of booking, hour and guest name stripping of all white spaces and converting to title case
        room = int(input("Room (101/102/201): ").strip())
        day = self.normalize_day(input("Day (Monday-Saturday): "))
        hour = int(input("Hour (9-17): ").strip())
        guest = input("Guest name: ").strip().title()
        # if inputs are not valid prints can not add booking
        if room not in ROOMS or day not in VALID_DAYS or hour not in VALID_HOURS or guest == "":
            print("Could not add booking.")
            return
        # new booking in same format as the slot key
        new_key = self.slot_key(day, room, hour)
        # if that certain slot is already filled prints can not add booking
        for b in self.bookings:
            if self.slot_key(b["Day"], b["Room"], b["Hour"]) == new_key:
                print("Could not add booking.")
                return
        # otherwise adds booking to the file
        self.bookings.append({"Day":day, "Room":room, "Hour":hour, "Guest":guest})
        print("Booking added.")


    def print_day_calendar(self, day):
        # sets variables
        day = self.normalize_day(day)
        times = [f"{h}:00" for h in range(9, 18)]
        rooms = ["101", "102", "201"]
        # creates empty calendar
        calendar = {time:{room: "empty" for room in rooms}for time in times}
        # adds bookings for that day in the correct places
        for b in self.bookings:
            if b["Day"] == day:
                time = f"{b['Hour']}:00"
                room = str(b["Room"])
                calendar[time][room] = b["Guest"]
        # prints calendar header and rows in proper format
        print()
        print(f"=== {day} Calender ===")
        print(f"{'Time':<15}{'101':<18}{'102':<18}{'201':<18}")
        for time in times:
            print(f"{time:<15}"
                  f"{calendar[time]['101']:<18}"
                  f"{calendar[time]['102']:<18}"
                  f"{calendar[time]['201']:<18}")


    def find_booking(self):
        # gets input for guest name
        guest = input("Guest name: ").strip().title()
        found = False
        # if guest name is found the associated information is extracted
        for b in self.bookings:
            if b["Guest"] == guest:
                found = True
                # information is printed
                print(f"{b['Guest'].title()} in Room {b['Room']} on {b['Day'].title()} at {b['Hour']}:00")
        if not found:
            print("No booking found.")


    def cancel_booking(self):
        # asks for room number, day and hour
        room = int(input("Room (101/102/201): ").strip())
        day = self.normalize_day(input("Day (Monday-Saturday): "))
        hour = int(input("Hour (9-17): ").strip())
        row = 0
        # loops until booking is found and match inputs
        while row < len(self.bookings):
            b = self.bookings[row]
            if b["Room"] == room and b["Day"] == day and b["Hour"] == hour:
                # removes booking from file
                self.bookings.pop(row)
                print("Booking cancelled.")
                return
            row += 1
        # if no booking found prints not found
        print("No booking found.")


    def change_booking(self):
        # asks for guest name
        guest = input("Guest name: ").strip().title()
        # finds booking via guest name
        for b in self.bookings:
            if b["Guest"].title() == guest:
                # asks for new room, day and hour
                new_room = int(input("New room: ").strip())
                new_day = self.normalize_day(input("New day: "))
                new_hour = int(input("New hour: ").strip())
                # ensures valid inputs
                if new_room not in ROOMS or new_day not in VALID_DAYS or new_hour not in VALID_HOURS:
                    print("Could not change booking.")
                    return
                # formats new booking information
                new_booking = self.slot_key(new_day, new_room, new_hour)
                # if new booking is equal to existing booking prints can not change booking
                for nb in self.bookings:
                    if nb ==b:
                        continue
                    if self.slot_key(nb["Day"], nb["Room"], nb["Hour"]) == new_booking:
                        print("Could not change booking.")
                        return
                # adds new booking to file while removing old booking
                b["Room"] = new_room
                b["Day"] = new_day
                b["Hour"] = new_hour
                print("Booking changed.")
                return
        print("No booking found.")


    def main(self):
        while True:
            # loops until "6" is entered breaking the loop and saving the program
            print()
            # prints options of program
            print("Simple Hotel Booking\n"
                  "1) Add booking\n"
                  "2) Show day calendar\n"
                  "3) Find booking by guest"
                  "4) Cancel booking\n"
                  "5) Change booking\n"
                  "6) Exit")
            option = input("Select option: ").strip()
            # loops through options until "6" is chosen then breaks loop
            if option == "1":
                self.add_booking()
            elif option == "2":
                day = self.normalize_day(input("Day (Monday-Saturday): "))
                self.print_day_calendar(day)
            elif option == "3":
                self.find_booking()
            elif option == "4":
                self.cancel_booking()
            elif option == "5":
                self.change_booking()
            elif option == "6":
                self.save_bookings()
                break
            else:
                print("Invalid option.")

HBS = HotelBookingSystem()
HBS.main()
