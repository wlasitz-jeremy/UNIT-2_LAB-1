import os


VALID_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
VALID_HOURS = range(9, 18)
ROOMS = [101, 102, 201]
FILE_NAME = "hotel_bookings.csv"

class HotelBookingSystem:
    def __init__(self):
        self.bookings = []
        self.load_bookings(FILE_NAME)


    def normalize_day(self, day):
        return day.strip().title()


    def slot_key(self, room, day, hour):
        day = self.normalize_day(day)
        return (room, day, hour)


    def load_bookings(self, path):
        if not os.path.exists(path):
            f = open(path, "w")
            f.write("Day,Room,Hour,Guest\n")
            f.close()

        f = open(path, "r")
        lines = f.readlines()
        f.close()

        for i in range(1, len(lines)):
            line = lines[i].strip()
            if line == "":
                continue

            parts = line.split(",")
            self.bookings.append({
                "Day": self.normalize_day(parts[0]),
                "Room": int(parts[1]),
                "Hour": int(parts[2]),
                "Guest": parts[3]
            })


    def save_bookings(self, path, bookings):
        bookings.sort(key=lambda b: (b["Day"], b["Hour"], b["Room"]))

        f = open(path, "w")
        f.write("Day,Room,Hour,Guest\n")

        for b in bookings:
            line = f"{b['Day']},{b['Room']},{b['Hour']},{b['Guest']}\n"
            f.write(line)

        f.close()


    def add_booking(self):
        room = int(input("Room (101/102/201): ").strip())
        day = self.normalize_day(input("Day (Monday-Saturday): "))
        hour = int(input("Hour (9-17): ").strip())
        guest = input("Guest name: ").strip().title()

        if room not in ROOMS or day not in VALID_DAYS or hour not in VALID_HOURS or guest == "":
            print("Could not add booking.")
            return

        new_key = self.slot_key(room, day, hour)

        for b in self.bookings:
            if self.slot_key(b["Room"], b["Day"], b["Hour"]) == new_key:
                print("Could not add booking.")
                return

        self.bookings.append({
            "Day": day,
            "Room": room,
            "Hour": hour,
            "Guest": guest
        })
        print("Booking added.")


    def print_day_calendar(self, bookings, day):
        day = self.normalize_day(day)

        print()
        print(f"=== {day} Calendar ===")

        header = f"{'Time':<15}"
        for room in ROOMS:
            header += f"{room:<18}"
        print(header)

        for hour in VALID_HOURS:
            row = f"{hour}:00".ljust(15)

            for room in ROOMS:
                guest = "empty"
                for b in bookings:
                    if self.slot_key(room, day, hour) == self.slot_key(b["Room"], b["Day"], b["Hour"]):
                        guest = b["Guest"]
                row += f"{guest:<18}"

            print(row)


    def find_booking(self):
        guest = input("Guest name: ").strip().title()
        found = False

        for b in self.bookings:
            if b["Guest"].title() == guest:
                print(f"Found: {b['Guest']} in room {b['Room']} on {b['Day']} at {b['Hour']}:00")
                found = True

        if not found:
            print("No booking found.")


    def cancel_booking(self):
        room = int(input("Room: ").strip())
        day = self.normalize_day(input("Day: "))
        hour = int(input("Hour: ").strip())

        target_key = self.slot_key(room, day, hour)

        for b in self.bookings:
            if self.slot_key(b["Room"], b["Day"], b["Hour"]) == target_key:
                self.bookings.remove(b)
                print("Cancelled.")
                return

        print("No booking found.")


    def change_booking(self):
        guest = input("Guest name: ").strip().title()

        for b in self.bookings:
            if b["Guest"].title() == guest:
                new_room = int(input("New room: ").strip())
                new_day = self.normalize_day(input("New day: "))
                new_hour = int(input("New hour: ").strip())

                if new_room not in ROOMS or new_day not in VALID_DAYS or new_hour not in VALID_HOURS:
                    print("Could not change booking.")
                    return

                new_key = self.slot_key(new_room, new_day, new_hour)

                for x in self.bookings:
                    if self.slot_key(x["Room"], x["Day"], x["Hour"]) == new_key:
                        print("Could not change booking.")
                        return

                b["Room"] = new_room
                b["Day"] = new_day
                b["Hour"] = new_hour
                print("Booking changed.")
                return

        print("No booking found.")


    def main(self):
        while True:
            print()
            print("Simple Hotel Booking")
            print("1) Add booking")
            print("2) Show day calendar")
            print("3) Find booking by guest")
            print("4) Cancel booking")
            print("5) Change booking")
            print("6) Exit")

            option = input("Select option: ").strip()

            if option == "1":
                self.add_booking()
            elif option == "2":
                self.print_day_calendar(self.bookings, day)
            elif option == "3":
                self.find_booking()
            elif option == "4":
                self.cancel_booking()
            elif option == "5":
                self.change_booking()
            elif option == "6":
                self.save_bookings(FILE_NAME, self.bookings)
                print("Saved. Goodbye.")
                break
            else:
                print("Invalid option.")


HotelBookingSystem().main()
