print(f"Welcome to Circle Phones' Profit Calculator.")
total_profit = 0.0
category = {1:120.45,
            2:99.50,
            3:75.69,
            4:65.73,
            5:51.49}
time_period = 1, 2, 3, 4





# 10,000 >= total_profit ---> "You did well this period! Keep up the great work!"
# 10,000 <= total_profit ---> "We didn't reach our goal for this period. More work is needed"

# print ('You can calculate the profit of the company according to a specific day or by a week ' + '\n'
#        'or divide the week into weekdays and weekend')


# Choosing
periodoftime = input(f'Enter: ' + '\n'
'1 - Specific Day \n'
'2 - For the week\n'
'3 - For Business Week \n'
'4 - For Weekend Days \n'
'0 - End\n')


# Specific Day
def specific_day():
    specific_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # Choosing Which Day
    days = input('Enter a specific day: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]' + '\n')
    # Conditions for Specific Day
    if days in specific_days:
        print(f'For {days}')
    else:
        print('Please select a valid day')


# def week():
#     # Conditions for Week Days
#     week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#     # Input for each day
#     for days in week_days:  # Figure out how to ask each day with each product sold
#
#
# # -----MAP-----
# # Choosing days etc.
# # Calculations for profit
# # Calling profit and days





while True:
    product_number = int(input('Enter product number 1-5, or enter 0 to stop:\n       ').strip())
    if product_number == 0:
        break
    if product_number in category:
        quantity_sold = int(input('Enter quantity sold:\n       ').strip())
        if quantity_sold < 0:
            print('Quantity sold must be greater than 0')
        total_profit += quantity_sold * category[product_number]
    else:
        print('Invalid input, please enter a valid number')
print(f"Your total profit for today is: {total_profit:.2f}")
