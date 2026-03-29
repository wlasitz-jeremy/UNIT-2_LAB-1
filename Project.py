import os

VALID_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
VALID_HOURS = range(9, 18)
ROOMS = [101, 102, 201]
FILE_NAME = "hotel_bookings.csv"


class HotelBookingSystem:
    def __init__(self):
        self.bookings = []
        self.load_bookings()

    # ---------- File Handling ----------
    def load_bookings(self):
        if not os.path.exists(FILE_NAME):
            f = open(FILE_NAME, "w")
            f.write("Day,Room,Hour,Guest\n")
            f.close()
            return

        f = open(FILE_NAME, "r")
        lines = f.readlines()
        f.close()

        for i in range(1, len(lines)):
            line = lines[i].strip()
            if line == "":
                continue
            parts = line.split(",")
            self.bookings.append({
                "Day": parts[0],
                "Room": int(parts[1]),
                "Hour": int(parts[2]),
                "Guest": parts[3]
            })

    def save_bookings(self):
        f = open(FILE_NAME, "w")
        f.write("Day,Room,Hour,Guest\n")
        for b in self.bookings:
            line = f"{b['Day']},{b['Room']},{b['Hour']},{b['Guest']}\n"
            f.write(line)
        f.close()

    # ---------- Features ----------
    def add_booking(self):
        room = int(input("Room: "))
        day = input("Day: ").strip().capitalize()
        hour = int(input("Hour: "))
        guest = input("Guest: ").strip()

        if room not in ROOMS or day not in VALID_DAYS or hour not in VALID_HOURS or guest == "":
            print("Could not add booking.")
            return

        for b in self.bookings:
            if b["Room"] == room and b["Day"] == day and b["Hour"] == hour:
                print("Could not add booking.")
                return

        self.bookings.append({
            "Day": day,
            "Room": room,
            "Hour": hour,
            "Guest": guest
        })
        print("Booking added.")

    def show_day_calendar(self):
        day = input("Day: ").strip().capitalize()
        print(f"=== {day} Calendar ===")

        for hour in VALID_HOURS:
            for room in ROOMS:
                guest = "Free"
                for b in self.bookings:
                    if b["Day"] == day and b["Room"] == room and b["Hour"] == hour:
                        guest = b["Guest"]
                print(f"{hour}:00 Room {room}: {guest}")
            print()

    def find_booking(self):
        guest = input("Guest name: ").strip().lower()
        found = False

        for b in self.bookings:
            if b["Guest"].lower() == guest:
                print(f"Found: {b['Guest']} in room {b['Room']} on {b['Day']} at {b['Hour']}:00")
                found = True

        if not found:
            print("No booking found.")

    def cancel_booking(self):
        room = int(input("Room: "))
        day = input("Day: ").strip().capitalize()
        hour = int(input("Hour: "))

        for b in self.bookings:
            if b["Room"] == room and b["Day"] == day and b["Hour"] == hour:
                self.bookings.remove(b)
                print("Cancelled.")
                return

        print("No booking found.")

    def change_booking(self):
        guest = input("Guest name: ").strip().lower()

        for b in self.bookings:
            if b["Guest"].lower() == guest:
                new_room = int(input("New room: "))
                new_day = input("New day: ").strip().capitalize()
                new_hour = int(input("New hour: "))

                if new_room not in ROOMS or new_day not in VALID_DAYS or new_hour not in VALID_HOURS:
                    print("Could not change booking.")
                    return

                for x in self.bookings:
                    if x["Room"] == new_room and x["Day"] == new_day and x["Hour"] == new_hour:
                        print("Could not change booking.")
                        return

                b["Room"] = new_room
                b["Day"] = new_day
                b["Hour"] = new_hour
                print("Booking changed.")
                return

        print("No booking found.")

    # ---------- Menu ----------
    def run(self):
        while True:
            print("\n1) Add booking")
            print("2) Show day calendar")
            print("3) Find booking")
            print("4) Cancel booking")
            print("5) Change booking")
            print("6) Exit")

            option = input("Select option: ")

            if option == "1":
                self.add_booking()
            elif option == "2":
                self.show_day_calendar()
            elif option == "3":
                self.find_booking()
            elif option == "4":
                self.cancel_booking()
            elif option == "5":
                self.change_booking()
            elif option == "6":
                self.save_bookings()
                print("Saved. Goodbye.")
                break
            else:
                print("Invalid option.")


HotelBookingSystem().run()