import os

VALID_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
VALID_HOURS = range(9, 18)
ROOMS = [101, 102, 201]
FILE_NAME = "hotel_bookings.csv"


class HotelBookingSystem:


    def __init__(self):
        self.bookings = []
        self.load_bookings(FILE_NAME)


    @staticmethod
    def normalize_day(day):
        return day.strip().title()


    def slot_key(self, day, room, hour):
        day = self.normalize_day(day)
        return day, room, hour


    def load_bookings(self, FILE_NAME):
        if not os.path.exists(FILE_NAME):
            return
        b = open(FILE_NAME, "r")
        content = b.readlines()
        b.close()
        for row in content:
            if row.strip() == "":
                continue
            day, room, hour, guest = row.strip().split(",")
            if day == "Day":
                continue
            self.bookings.append({
                "Day": day,
                "Room": int(room),
                "Hour": int(hour),
                "Guest": guest})


    def save_bookings(self):
        b = open(FILE_NAME, "w")
        b.write("Day,Room,Hour,Guest\n")
        for booking in self.bookings:
            line = f"{booking['Day']},{booking['Room']},{booking['Hour']},{booking['Guest']}"
            b.write(line + "\n")
        b.close()
        print("Saved. Goodbye.")


    def add_booking(self):
        room = int(input("Room (101/102/201): ").strip())
        day = self.normalize_day(input("Day (Monday-Saturday): "))
        hour = int(input("Hour (9-17): ").strip())
        guest = input("Guest name: ").strip().title()
        if room not in ROOMS or day not in VALID_DAYS or hour not in VALID_HOURS or guest == "":
            print("Could not add booking.")
            return
        new_key = self.slot_key(day, room, hour)
        for b in self.bookings:
            if self.slot_key(b["Day"], b["Room"], b["Hour"]) == new_key:
                print("Could not add booking.")
                return
        self.bookings.append({"Day":day, "Room":room, "Hour":hour, "Guest":guest})
        print("Booking added.")


    def print_day_calendar(self, day):
        day = self.normalize_day(day)
        times = [f"{h}:00" for h in range(9, 18)]
        rooms = ["101", "102", "201"]
        calendar = {time:{room: "empty" for room in rooms}for time in times}
        for b in self.bookings:
            if b["Day"] == day:
                time = f"{b['Hour']}:00"
                room = str(b["Room"])
                calendar[time][room] = b["Guest"]
        print()
        print(f"=== {day} Calender ===")
        print(f"{'Time':<15}{'101':<18}{'102':<18}{'201':<18}")
        for time in times:
            print(f"{time:<15}"
                  f"{calendar[time]['101']:<18}"
                  f"{calendar[time]['102']:<18}"
                  f"{calendar[time]['201']:<18}")


    def find_booking(self):
        guest = input("Guest name: ").strip().title()
        found = False
        for b in self.bookings:
            if b["Guest"] == guest:
                found = True
                print(f"{b['Guest'].title()} in Room {b['Room']} on {b['Day'].title()} at {b['Hour']}:00")
        if not found:
            print("No booking found.")


    def cancel_booking(self):
        room = int(input("Room (101/102/201): ").strip())
        day = self.normalize_day(input("Day (Monday-Saturday): "))
        hour = int(input("Hour (9-17): ").strip())
        i = 0
        while i < len(self.bookings):
            b = self.bookings[i]
            if b["Room"] == room and b["Day"] == day and b["Hour"] == hour:
                self.bookings.pop(i)
                print("Booking cancelled.")
                return
            i += 1
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
                new_booking = self.slot_key(new_day, new_room, new_hour)
                for nb in self.bookings:
                    if nb ==b:
                        continue
                    if self.slot_key(nb["Day"], nb["Room"], nb["Hour"]) == new_booking:
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

HotelBookingSystem().main()
