import os


VALID_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
VALID_HOURS = range(9, 18)
ROOMS = [101, 102, 201]
FILE_NAME = "hotel_bookings.csv"

class HotelBookingSystem:
    def __init__(self):
        self.bookings = []
        self.load_bookings()


    def normalize_day(self, day):
        return day.strip().title()


    def slot_key(self, day, room, hour):
        day = self.normalize_day(day)
        return day, room, hour


    def load_bookings(self):
        pass


    def save_bookings(self):
        pass


    def add_booking(self):
        pass


    def print_day_calendar(self):
        pass


    def find_booking(self):
        pass


    def cancel_booking(self):
        pass


    def change_booking(self):
       pass


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
                self.print_day_calendar()
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


HotelBookingSystem().main()
