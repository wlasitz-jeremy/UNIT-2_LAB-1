print(f"Welcome to Circle Phones' Profit Calculator.")
product_number = [0,1,2,3,4,5]
quantity_sold = 0
total_profit = 0
category = {'applephone', 120.45,
     'androidphone', 99.50,
     'appletablet', 75.69,
     'androidtablet', 65.73,
     'windowstablet', 51.49}
while product_number !='0':
    product_number = input('Enter product number 1-5, or enter 0 to stop: ')
    quantity_sold = float(input('Enter quantity sold: '))
    if product_number == '0':
        break
if product_number==product_number:
    total_profit = product_number * quantity_sold
    print(f"Your total profit for today is {total_profit:.2f}")
else:
    print(f"Invalid input, please enter a valid number")
