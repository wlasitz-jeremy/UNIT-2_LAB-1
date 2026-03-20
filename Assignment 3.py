def view_flights():
    file = open('flights.csv', 'r')
    content = file.readline()
    while content != "":
        content = content.strip().split(",")
        print("{:<15} {:<12} {:<15} {:<17} {:<10}".format(content[0], content[1], content[2], content[3], content[4]))
        content = file.readline()
    file.close()

def main():

    print("Welcome to the Flight Viewer\n"
        "1. View Flights\n"
        "2. Book Flights\n"
        "3. View Bookings\n"
        "4. Cancel Bookings\n"
        "5. Exit"
        )
main()
choice = input("Enter number between 1 and 4: ")

if choice == '1':
    view_flights()



elif choice == '2':
    file = open('flights.csv', 'a')



elif choice == '3':
    file = open('flights.csv', 'r')



elif choice == '4':
    file = open('flights.csv', 'a')



else:
    exit()



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
