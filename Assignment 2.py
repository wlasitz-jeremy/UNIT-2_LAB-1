print(f"Welcome to Circle Phones' Profit Calculator.")
total_profit = 0.0
category = {
    1: ('applephone', 120.45,),
    2: ('androidphone', 99.50,),
    3: ('appletablet', 75.69,),
    4: ('androidtablet', 65.73,),
    5: ('windowstablet', 51.49)
    }
while True:
    product_number = input('Enter product number 1-5, or enter 0 to stop:\n       ').strip()
    if product_number =='0':
        break
    if product_number in category:
        continue
    else:
        print('Invalid input, please enter a valid number')
    product_number = int(product_number)
    quantity_sold = input('Enter quantity sold:\n       ').strip()
    if not quantity_sold.isdigit():
        print('Invalid input, please enter 0 or more')
        continue
    quantity_sold = int(quantity_sold)
    if quantity_sold < 0:
        print('Quantity sold must be greater than 0')
        continue
