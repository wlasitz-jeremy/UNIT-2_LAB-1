# print(f"Welcome to Circle Phones' Profit Calculator.")
# total_profit = 0.0
# category = {1:120.45,
#             2:99.50,
#             3:75.69,
#             4:65.73,
#             5:51.49}
# time_period = 1, 2, 3, 4
# while True:
#     product_number = int(input('Enter product number 1-5, or enter 0 to stop:\n       ').strip())
#     if product_number == 0:
#         break
#     if product_number in category:
#         quantity_sold = int(input('Enter quantity sold:\n       ').strip())
#         if quantity_sold < 0:
#             print('Quantity sold must be greater than 0')
#         total_profit += quantity_sold * category[product_number]
#     else:
#         print('Invalid input, please enter a valid number')
# print(f"Your total profit for today is: {total_profit:.2f}")



# CPRG 216 - Profit Calculator

# Welcome Message
print("Welcome to Circle Phones' Profit calculator. You can calculate your profits for a specific day, by week or you can divide the week into weekdays and the weekend.")

# Main program loop
time_period = ""
while time_period != "0":

    # Display menu
    print("You can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend")
    print("Enter:")
    print("1 - For specific Day")
    print("2 - For the Week")
    print("3 - For Week Business Days")
    print("4 - For Weekend days")
    print("0 - Exit")

    time_period = input()

    # Making sure the input is a valid number
    if not time_period.isdigit() and time_period != "0":
        print("Invalid input, please enter a valid input")
    elif time_period == "0":
        print("Program End!")
    elif time_period == "1" or time_period == "2" or time_period == "3" or time_period == "4":

        # Initialize variables
        total_profit = 0.0

        # Determine which days to loop through depending on what the user choose
        if time_period == "1":
            print(
                "Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]")
            day_input = input()
            day_name = day_input.strip().title()
            days = [day_name]
        elif time_period == "2":
            days = ["Monday", "Tuesday", "Wednesday",
                    "Thursday", "Friday", "Saturday", "Sunday"]
        elif time_period == "3":
            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        elif time_period == "4":
            days = ["Saturday", "Sunday"]

        # Loop through every single day
        for day in days:
            print(f"For {day}")

            # Product number input
            category_input = input("Enter product number 1-5 or 0 to stop:\n")

            # Making sure the input is a valid number
            while not category_input.isdigit():
                print("Invalid input, please enter a valid number")
                category_input = input(
                    "Enter product number 1-5 or 0 to stop:\n")

            category = int(category_input)

            # Loop until category=0
            while category != 0:
                # category >=1 and <=5?
                if category >= 1 and category <= 5:
                    # Enter Qty Sold
                    quantity_input = input("Enter quantity sold:\n")

                    # Making sure the input is a valid number before making it an interger number
                    while not quantity_input.isdigit():
                        print("Invalid input, please enter a valid number")
                        quantity_input = input("Enter quantity sold:\n")

                    quantity = int(quantity_input)

                    # categories
                    if category == 1:
                        profit = quantity * 120.45
                    elif category == 2:
                        profit = quantity * 99.50
                    elif category == 3:
                        profit = quantity * 75.69
                    elif category == 4:
                        profit = quantity * 65.73
                    else:
                        profit = quantity * 51.49

                    # totalprofit=totalprofit+profit
                    total_profit = total_profit + profit
                else:
                    # Invalid Category
                    print("Invalid input, please enter a valid number")

                # Loop back to Enter product number
                category_input = input(
                    "Enter product number 1-5 or 0 to stop:\n")

                while not category_input.isdigit():
                    print("Invalid input, please enter a valid number")
                    category_input = input(
                        "Enter product number 1-5 or 0 to stop:\n")

                category = int(category_input)

        # Display total profit and comment based on time period
        if time_period == "1":
            day_name = days[0]
            print(f"Total Profit for the {day_name} is: ${total_profit:.2f}")
            if total_profit >= 10000:
                print(f"You did good this {day_name}")
            else:
                print(
                    f"More hard work needed... The last {day_name} wasn't the best")
        elif time_period == "2":
            print(f"Total Profit for the week is: ${total_profit:.2f}")
            if total_profit >= 10000:
                print("You did good this week")
            else:
                print("More hard work needed... The last week wasn't the best")
        elif time_period == "3":
            print(
                f"Total Profit for the week (business days) is: ${total_profit:.2f}")
            if total_profit >= 10000:
                print("You did good this week (business days)")
            else:
                print(
                    "More hard work needed... The last week (business days) wasn't the best")
        elif time_period == "4":
            print(f"Total Profit for the weekend is: ${total_profit:.2f}")
            if total_profit >= 10000:
                print("You did good this weekend")
            else:
                print("More hard work needed... The last weekend wasn't the best")
    else:
        print("Invalid input, please enter a valid input")
