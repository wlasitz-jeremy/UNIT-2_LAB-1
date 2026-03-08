print(f"Welcome to Circle Phones' Profit Calculator.")
total_profit = 0.0
quantity_sold = 0.0
product_number = 0.0
category = {
    1:120.45,
    2:99.50,
    3:75.69,
    4:65.73,
    5:51.49
}
while True:
    product_number = int(input('Enter product number 1-5, or enter 0 to stop:\n       ').strip())
    if product_number == 0:
        break
    if product_number in category:
        quantity_sold = int(input('Enter quantity sold:\n       ').strip())

        if quantity_sold < 0:
            print('Quantity sold must be greater than 0')
            continue
        total_profit += quantity_sold * category[product_number]
    else:
        print('Invalid input, please enter a valid number')
print(f"Your total profit for today is: {total_profit:.2f}")
