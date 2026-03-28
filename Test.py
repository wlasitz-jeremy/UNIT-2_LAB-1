# current_price=float(input('Enter the current price '))
# last_month_price=float(input('Enter the last months price '))
# change_of_price=current_price-last_month_price
# monthly_mortgage=float(current_price)*(0.051)/12
# print(f'Current price is: {current_price}\nChange of price since last month is: {change_of_price}\nEstimated monthly mortage is: {monthly_mortgage}')
from xml.sax.handler import property_lexical_handler


# r = float(input('Enter radius '))
# h = float(input('Enter height '))
# pi=3.14
# volume=str(pi*(r**2)*h)
# area=str((2*pi)*h*r + pi*(r**2))
# print("Area="+area+"\nVolume="+volume)




# sd=float(input('Enter starting distance '))
# ed=float(input('Enter stopping distance '))
# st=float(input('Enter starting time '))
# et=float(input('Enter stopping time '))
# d=ed-sd
# t=et-st
# v1=sd/st
# v2=ed/et
# cv=float(v2)-float(v1)
# a=float(cv)/float(t)
# print(f'"Velocity="{v2}m/s\nAccelleration="{a}m/s**2')




# num = float(input('Enter a number'))
# if num % 2 == 0:
#     print(str(num) + ' is even')
#     print(str(num) + ' is absolute')
# else:
#     print(str(num) + " is odd")
#     print(str(num) + ' is not absolute')




# grd = int(input('Enter grade point'))
# if grd>90 and grd<=100:
#     print(f'A+')
# elif grd>85 and grd<=89:
#     print(f'A')
# elif grd>80 and grd<=84:
#     print(f'A-')
# elif grd>77 and grd<=79:
#     print(f'B+')
# elif grd>73 and grd<=76:
#     print(f'B')
# elif 70<grd<72:
#     print(f'B-')
# elif grd>67 and grd<=69:
#     print(f'C+')
# elif grd>63 and grd<=66:
#     print(f'C')
# elif grd>60 and grd<=62:
#     print(f'C-')
# elif grd>55 and grd<=59:
#     print(f'D+')
# elif grd>50 and grd<=54:
#     print(f'D')
# else:
#     print(f'F')




# yr = int(input('Enter year: '))
# if yr%4==0:
#     if yr%100==0 or yr%400==0:
#         print(f'{yr} is not a leap year')
#     else:
#         print(f'{yr} is a leap year')
# else:
#     print(f'{yr} is not a leap year')




# course = 'Python'
# print(f'{course:>20}')
# print(f'{course:<20}')
# print(f'{course:20}')
# print(f'{"Centered":^20}\n')
# cadtd= 1.2798
# usdtd= 0.940
# cadytd= 2.7843
# usdytd= 2.050
# changeusd= (usdtd-usdytd)
# changecad= (cadtd-cadytd)
# print(f'{"Date":^10}{"Rate":^20}')
# print(f'Cad Yesterday{cadytd:^17.4f}')
# print(f'Cad Today{cadtd:^24.4f}')
# print(f'Cad Change{changecad:^22.4f}')
# print(f'Usd Yesterday{usdytd:^16.4f}')
# print(f'Usd Today{cadtd:^24.4f}')
# print(f'Usd Change{changeusd:^22.4f}')
# num=2
# while num<=512:
#     print(num)
#     num+=2




# kpm=1.61
# print(f'{"MPH"}',f'{"KPH":>10}')
# print('==========',"==========")
# for mph in range(10,80,10):
#     kph=mph*kpm
#     print(f'{mph:10d}{kph:>10.0f}')
# for i in range (1,3):
#     for j in range (1,3):
#         print(f'{i}*{j}=',i*j)




# RC='Rock Climbing'
# print(RC[5:10])
# for height in range(0,len(RC)):
#     print(RC[height-8])
# height=0
# while height<len(RC):
#     print(RC[height])
#     height+=2
# print(RC.upper())
# print(RC.lower())
# course=input("Enter course name: ")
# alpha=0
# beta=0
# charlie=0
# for charlie in course:
#     if course.isalpha():
#         alpha+=1
#     else:
#         if course.isalnum():
#             beta+=1
# print(alpha,beta)




# names=('Joe', 'Ed', 'Fred')
# num=len(names)
# print(num)
# first=min(names)
# print(first)
# print(max(names))
# del names




# days=('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')
# print(days)
# weekdays=(f'Weekdays:{days[1:5]}')
# print(weekdays)
# weekends=(f'Weekends:{days[0]} {days[6]}')
# print(weekends)




# def show_welcome():
#     """ Function to show welcome message """
#     print("Hello to the library!")
# def display_books():
#     """ Function to display books """
#     print("Here are our books...")
# def issue_books():
#     """ Function to issue books """
#     print("This book is for you!")
# def return_books():
#     """ Function to return books """
#     print("Thank-you for returning the books!")
# print(f"{show_welcome.__doc__}\n"
#       f"{display_books.__doc__}\n"
#       f"{issue_books.__doc__}\n"
#       f"{return_books.__doc__}\n")
# show_welcome()
# display_books()
# issue_books()
# return_books()




# def total(value1,value2):
#     total=0
#     '''sum of numbers'''
#     total=int(value1)+int(value2)
#     print(f"The sum of the numbers is: {total}")
# value1=input("Enter first number: ")
# value2=input("Enter second number: ")
# print(total.__doc__)
# total(value1,value2)




# def student(name,mark1,mark2,mark3):
#     average_mark = 0
#     average_mark = (mark1 + mark2 + mark3) / 3
#     print(f"Your average mark is {average_mark}")
# name = str(input("Enter your name: "))
# mark1 = float(input("Enter your mark: "))
# mark2 = float(input("Enter your mark: "))
# mark3 = float(input("Enter your mark: "))
# student(name,mark1,mark2,mark3)




# def celsius_to_fahrenheit():
#     c = float(input(f"Input your temperature in Celsius: "))
#     f = (9/5)*c+32
#     print(f"Your temperature in Fahrenheit is {f:.1f}")
# def fahrenheit_to_celsius():
#     f = float(input(f"Input your temperature in Fahrenheit: "))
#     c = (f-32)*(5/9)
#     print(f"Your temperature in Celsius is {c:.1f}")
# celsius_to_fahrenheit()
# fahrenheit_to_celsius()




# category = {
#     1: 120.45,
#     2: 99.50,
#     3: 75.69,
#     4: 65.73,
#     5: 51.49
# }
# product_number = int(input('Enter product number:\n       ').strip())
# if product_number in category:
#     print(category[product_number])
# else:
#     print('Try Again')




# quantity_sold = int(input("Please enter the quantity sold:\n       ").strip())
# if quantity_sold < 0:
#     print("Sorry, you can't solve for negative quantity")
# else:
#     print(f"You sold {quantity_sold}")



# testfile = open('C://SAIT//Object Oriented Programming 1 CPRG-216//testfile.txt', mode='w')
# line = "Hello World\n","This is pretty cool\n","I kinda love coding!"
# testfile.writelines(line)
# testfile.close()
# testfile = open('C://SAIT//Object Oriented Programming 1 CPRG-216//testfile.txt', mode='r')
# content = testfile.read()
# print(content)
# testfile.close()
#
#
#
#
# file = open('C://SAIT//Object Oriented Programming 1 CPRG-216//testfile.txt', 'r')
# line = file.readline()
# while line != '':
#     line = line.strip()
#     print(line)
#     line = file.readline()
# file.close()




# import os
# cwd = os.getcwd()
# print(cwd)
# file_path = os.path.join(cwd, "example.txt")
# print(file_path)
# exists = os.path.exists(file_path)
# print(exists)
# os.mkdir('my_directory')
# import os
# file_name = input("Enter file name: ")
# if os.path.exists(file_name):
#     print("The file Exists")
# else:
#     print("The file does not exist")




# file = open('temp_file.csv', 'r')
# file.readline()
# totalmaxtemp = 0
# numbertemp = 0
# content = file.readline()
# while content != "":
#     items = content.rstrip().split(",")
#     maxstring = items[9]
#     if maxstring != "":
#         maxtemp = float(maxstring)
#         totalmaxtemp += maxtemp
#         numbertemp += 1
#         content = file.readline()
# file.close()
# average_temp = totalmaxtemp / numbertemp
# print(f"{average_temp:.2f}")




# def countdown(n):
#     n -= 1
#     if n == 0:
#         print(n)
#     else:
#         countdown(n)
# n = int(input("Please enter a number: "))
# countdown(n)




# def gcd(x, y):
#     if y == 0:
#         return x
#     else:
#         return gcd(y, x % y)
#
# n1 = int(input("Enter first positive number: "))
# n2 = int(input("Enter second positive number: "))
#
# result = gcd(n1, n2)
# print(f"The GCD is {result}")




# class Human:
#     def __init__(self, name, age, email):
#         self.name = name
#         self.age = age
#         self.email = email
#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return self.age
#     def get_email(self):
#         return self.email
#     def print_info(self):
#         print(f"Name = {jeremy.name}\nAge = {jeremy.age}\nEmail = {jeremy.email}")
#
# jeremy = Human("Jeremy Wlasitz", 21, "jeremy.wlasitz@edu.sait.ca")
# print(f"{jeremy.get_name()}\n"
#       f"{jeremy.get_age()}\n"
#       f"{jeremy.get_email()}\n")
# print(jeremy.print_info())




# class Rectangle:
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length
#     def get_width(self):
#         return self.width
#     def get_length(self):
#         return self.length
#     def set_width(self, new_width):
#         self.width = new_width
#     def set_length(self, new_length):
#         self.length = new_length
#     def perimeter(self):
#         return int(self.width) * 2 + int(self.length) * 2
#     def area(self):
#         return int(self.width) * int(self.length)
# width = input("Enter the width:\n")
# length = input("Enter the height:\n")
# x = Rectangle(width, length)
# print(x.perimeter())
# print(x.area())




# # Flight Booking System
# # CPRG 216 - Assignment 4: Functions, Scoping and Abstraction
#
# # Start importing os toolbox so we can check if a file exists
# import os
#
# # Constants
# FLIGHT_NUM_IDX = 0
# SOURCE_IDX = 1
# DEST_IDX = 2
# SEATS_IDX = 3
# PRICE_IDX = 4
#
#
# # File read and it breakdown into single elements
# def load_flights(file_name):
#     flights = []
#     with open(file_name, "r") as f:
#         for line in f:
#             line = line.strip()
#             if line != "":
#                 parts = line.split(",")
#                 flight = [
#                     parts[0].strip(),
#                     parts[1].strip(),
#                     parts[2].strip(),
#                     int(parts[3].strip()),
#                     float(parts[4].strip())
#                 ]
#                 flights.append(flight)
#     return flights
#
#
# # Converts flights back to text and writes them to the file
# def save_flights(file_name, flights):
#     with open(file_name, "w") as f:
#         for flight in flights:
#             line = (flight[FLIGHT_NUM_IDX] + "," +
#                     flight[SOURCE_IDX] + "," +
#                     flight[DEST_IDX] + "," +
#                     str(flight[SEATS_IDX]) + "," +
#                     str(flight[PRICE_IDX]) + "\n")
#             f.write(line)
#
#
# # Display all available flights in a formatted table
# def view_flights(flights):
#     print("\n" + "-" * 65)
#     print("{:<12} {:<15} {:<15} {:<10} {}".format(
#         "Flight No", "Source", "Destination", "Seats", "Price ($)"))
#     print("-" * 65)
#     for flight in flights:
#         print("{:<12} {:<15} {:<15} {:<10} {:.2f}".format(
#             flight[FLIGHT_NUM_IDX],
#             flight[SOURCE_IDX],
#             flight[DEST_IDX],
#             flight[SEATS_IDX],
#             flight[PRICE_IDX]))
#     print("-" * 65)
#
#
# # Finds the flight, checks seats, saves booking if successful
# def book_flight(passenger_name, file_name, flights, bookings):
#     flight_num = input("Enter flight number: ").strip()
#
#     found_flight = None
#     for flight in flights:
#         if flight[FLIGHT_NUM_IDX].upper() == flight_num.upper():
#             found_flight = flight
#             break
#
#     if found_flight is not None:
#         seats_requested = int(input("Enter number of seats to book: "))
#         if seats_requested <= found_flight[SEATS_IDX]:
#             found_flight[SEATS_IDX] -= seats_requested
#             save_flights(file_name, flights)
#             booking = (passenger_name + "," +
#                        found_flight[FLIGHT_NUM_IDX] + "," + str(seats_requested))
#             bookings.append(booking)
#             print("Booking confirmed! You booked " + str(seats_requested) +
#                   " seat(s) on flight " + found_flight[FLIGHT_NUM_IDX] + ".")
#         else:
#             print("Not enough seats available. Only " +
#                   str(found_flight[SEATS_IDX]) + " seat(s) remaining.")
#     else:
#         print("Flight not found.")
#
#
# # Finds and displays all bookings that belong to this passenger
# def view_bookings(passenger_name, bookings):
#     booking_found = False
#     print("\n--- Your Bookings ---")
#     for booking in bookings:
#         parts = booking.split(",")
#         if parts[0].strip().lower() == passenger_name.strip().lower():
#             booking_found = True
#             print("Flight: " + parts[1].strip() +
#                   "  |  Seats Booked: " + parts[2].strip())
#     if not booking_found:
#         print("You have no bookings.")
#
#
# # Finds the booking, restores the seats, and removes it from the list
# def cancel_booking(passenger_name, file_name, flights, bookings):
#     flight_num = input("Enter flight number to cancel: ").strip()
#
#     booking_to_cancel = None
#     for booking in bookings:
#         parts = booking.split(",")
#         if (parts[0].strip().lower() == passenger_name.strip().lower() and
#                 parts[1].strip().upper() == flight_num.upper()):
#             booking_to_cancel = booking
#             break
#
#     if booking_to_cancel is not None:
#         parts = booking_to_cancel.split(",")
#         seats_to_restore = int(parts[2].strip())
#
#         for flight in flights:
#             if flight[FLIGHT_NUM_IDX].upper() == flight_num.upper():
#                 flight[SEATS_IDX] += seats_to_restore
#                 break
#
#         save_flights(file_name, flights)
#         bookings.remove(booking_to_cancel)
#         print("Booking for flight " + flight_num + " cancelled. " +
#               str(seats_to_restore) + " seat(s) returned.")
#     else:
#         print("Booking not found.")
#
#
# # Shows the menu options and returns what the user picked
# def main_menu():
#     print("\n========== Flight Booking System ==========")
#     print("1. View Available Flights")
#     print("2. Book a Flight")
#     print("3. View My Bookings")
#     print("4. Cancel a Booking")
#     print("5. Exit")
#     return input("Select an option (1-5): ").strip()
#
#
# # Runs the whole program from start to finish
# def main():
#     print("============================================")
#     print("   Welcome to the Flight Booking System!   ")
#     print("============================================")
#
#     # Ask for file name; re-prompt if file does not exist
#     file_name = input("Enter the flights data filename: ").strip()
#     while not os.path.exists(file_name):
#         print("Error: File '" + file_name + "' not found. Please try again.")
#         file_name = input("Enter the flights data filename: ").strip()
#
#     flights = load_flights(file_name)
#     bookings = []
#
#     passenger_name = input("Enter your name: ").strip()
#
#     option = main_menu()
#     while option != "5":
#         if option == "1":
#             view_flights(flights)
#         elif option == "2":
#             book_flight(passenger_name, file_name, flights, bookings)
#         elif option == "3":
#             view_bookings(passenger_name, bookings)
#         elif option == "4":
#             cancel_booking(passenger_name, file_name, flights, bookings)
#         else:
#             print("Invalid option. Please enter a number between 1 and 5.")
#         option = main_menu()
#
#     print("\nThank you for using the Flight Booking System. Goodbye!")
#
# # Start the program
# main()




# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"
# def main():
#     individual = []
#     while True:
#         name = input("Enter your name: ").strip()
#         age = input("Enter your age: ").strip()
#         if name == "":
#             break
#         p = Person(name, age)
#         individual.append(p)
#     for person in individual:
#         print(person)
# main()




# Pseudocode
# input filename
# student_file = open filename
# create empty Students list
# total_score = average = 0
# read all items in student_file
# 	items = next line split up
# 	grade = item 2
# 	create Student object st with item 0, item 1 and grade
# 	append st to students list
# 	total_score += grade
# close student_file
# average = total_score/length of the students list
# print average
# for i in range of the number of students
# 	if students[i] grade > average
# 		print students[i]
# import os
# file_name = input("Enter file name: ")
# if os.path.exists(file_name):
#     class Student:
#         def __init__(self, f_name, l_name, grade):
#             self.f_name = f_name
#             self.l_name = l_name
#             self.grade = grade
#         def __str__(self):
#             return f"{self.f_name:<5}{self.l_name:<5}{self.grade:<5}"
# else:
#     print("File doesn't exist")
# def main():
#     s = open(file_name, "r")
#     content = s.readlines()
#     student = []
#     totalscore = average = 0
#     while True:
#         f_name = input("Enter first name: ").strip()
#         l_name = input("Enter last name: ").strip()
#         grade = input("Enter grade: ")
#         print("Enter '0' to exit")
#         if f_name =="0":
#             break
#     st = Student(f_name, l_name, grade)
#     student.append(st)
#     totalscore += int(grade)
#     average = totalscore / len(student)
#     print(f"{"First":<5} {"Last":<5} {"Grade":<5}")
#     print(f"{f_name:<5} {l_name:<5} {average[0]:<5}")
#     s.close()
# main()




# class Employees:
#
#     number_of_employees = 0
#
#     def __init__(self, name, hourly_rate, hours_worked):
#         self.name = name
#         self.hourly_rate = hourly_rate
#         self.hours_worked = hours_worked
#         Employees.number_of_employees += 1
#
#
#
#     def __str__(self):
#         return (f"Payroll report for {self.name}\n"
#                 f"Hours = {self.hourly_rate}\n"
#                 f"Rate = {self.hourly_rate}\n"
#                 f"Total Gross = {total_hours_worked()}\n")
#
#
#
#     def get_name(self):
#         return self.name
#
#     def get_hourly_rate(self):
#         return self.hourly_rate
#
#     def get_hours_worked(self):
#         return self.hours_worked
#
#
#
#     def set_name(self, name):
#         self.name = name
#
#     def set_hourly_rate(self, hourly_rate):
#         self.hourly_rate = hourly_rate
#
#     def set_hours_worked(self, hours_worked):
#         self.hours_worked = hours_worked
#
#
#
#     def add_hours_worked(self, hours_worked):
#         self.hours_worked += hours_worked
#
#     def calc_total_hours_worked(self):
#         hours_worked * hourly_rate = total_hours_worked
#
#
# e = Employees("Sara", 15, 40)
# e2 = Employees("Harvey", 11.20, 15)
# print(e)
# print(e2)
