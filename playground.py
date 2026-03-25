import os
import csv

BOOKING_FILE = "hotel_bookings.csv"


class Booking:
    def __init__(self, day, room, hour, guest):
        self.day = day
        self.room = room
        self.hour = hour
        self.guest = guest

    def to_list(self):
        return [self.day, self.room, self.hour, self.guest]


class BookingSystem:

    VALID_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    VALID_ROOMS = ["101", "102", "201"]

    def __init__(self):
        self.bookings = []
        self.load_bookings()


    def normalize_day(self, day):
        if not day:
            return None
        d = day.strip().title()
        return d if d in self.VALID_DAYS else None


    def slot_key(self, room, day, hour):
        return (day, room, str(hour))


    def load_bookings(self, path=BOOKING_FILE):
        self.bookings = []

        if not os.path.exists(path):
            with open(path, "w", newline="") as f:
                csv.writer(f).writerow(["Day", "Room", "Hour", "Guest"])
            return

        with open(path, "r", newline="") as f:
            reader = csv.reader(f)
            next(reader, None)  # skip header
            for row in reader:
                if len(row) == 4:
                    self.bookings.append(Booking(*row))


    def save_bookings(self, path=BOOKING_FILE):
        sorted_rows = sorted(
            (b.to_list() for b in self.bookings),
            key=lambda x: (x[0], x[1], int(x[2]))
        )

        with open(path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Day", "Room", "Hour", "Guest"])
            writer.writerows(sorted_rows)


    def print_day_calendar(self):
        day = self.normalize_day(input("Day (Monday-Saturday): "))
        if not day:
            print("Invalid day.")
            return

        print(f"=== {day} Calendar ===")
        print("Time\t101\t102\t201")

        lookup = {(b.day, b.room, b.hour): b.guest for b in self.bookings}

        for hour in range(9, 18):
            entries = []
            for room in self.VALID_ROOMS:
                guest = lookup.get((day, room, str(hour)), "empty")
                entries.append(guest)
            print(f"{hour}:00\t" + "\t".join(entries))


    def add_booking(self):
        room = input("Room number (101/102/201): ").strip()
        if room not in self.VALID_ROOMS:
            print("Invalid room.")
            return

        day = self.normalize_day(input("Day (Monday-Saturday): "))
        if not day:
            print("Invalid day.")
            return

        hour = input("Hour (9-17): ").strip()
        if not hour.isdigit() or not (9 <= int(hour) <= 17):
            print("Invalid hour.")
            return

        guest = input("Guest name: ").strip().title()

        key = self.slot_key(room, day, hour)

        for b in self.bookings:
            if (b.day, b.room, b.hour) == key:
                print("Could not add booking — conflict.")
                return

        self.bookings.append(Booking(day, room, hour, guest))
        self.save_bookings()
        print("Booking added.")


    def find_booking(self):
        guest = input("Guest name: ").strip().title()
        found = False

        for b in self.bookings:
            if b.guest == guest:
                print(f"{guest} is in Room {b.room} on {b.day} at {b.hour}:00")
                found = True

        if not found:
            print("No booking found.")


    def cancel_booking(self):
        guest = input("Guest name to cancel: ").strip().title()

        original_count = len(self.bookings)
        self.bookings = [b for b in self.bookings if b.guest != guest]

        if len(self.bookings) < original_count:
            self.save_bookings()
            print("Booking canceled.")
        else:
            print("No booking found.")


    def change_booking(self):
        guest = input("Guest name to change: ").strip().title()
        found = False

        for b in self.bookings:
            if b.guest == guest:
                print(f"Found: {b.day}, {b.hour}:00, Room {b.room}")
                found = True

        if not found:
            print("No booking found.")
            return


        self.bookings = [b for b in self.bookings if b.guest != guest]
        self.save_bookings()
        print("Old booking removed.")

        print("Enter NEW booking:")
        self.add_booking()




system = BookingSystem()

print(f"Simple Hotel Booking\n"
      f"1) Add booking\n"
      f"2) Show day calender\n"
      f"3) Find booking by guest\n"
      f"4) Cancel booking\n"
      f"5) Change booking\n"
      f"6) Exit")

option = input("Select option: ").strip()

while option != "6":

    if option == "1":
        system.add_booking()

    elif option == "2":
        system.print_day_calendar()

    elif option == "3":
        system.find_booking()

    elif option == "4":
        system.cancel_booking()

    elif option == "5":
        system.change_booking()

    else:
        print("Invalid choice, enter 1 to 6")

    print()
    print(f"Simple Hotel Booking\n"
          f"1) Add booking\n"
          f"2) Show day calender\n"
          f"3) Find booking by guest\n"
          f"4) Cancel booking\n"
          f"5) Change booking\n"
          f"6) Exit")

    option = input("Select option: ").strip()

print("Saved. Goodbye.")
