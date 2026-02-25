print(f"Welcome to Circle Phones' Profit Calculator.\n")
product_number = [0,1,2,3,4,5]
quantity_sold = 0
total_profit = 0
1 = {applephone, 120.45}
2 = {nadroidphone, 99.50}
3 = {appletablet, 75.69}
4 = {androidtablet, 65.73}
5 = {windowstablet, 51.49}
while product_number !='o':
    product_number = input('Enter product number 1-5, or enter 0 to stop: '
                           '')
    quantity_sold = input('Enter quantity sold: '
                          '')
if product_number==product_number:
    total_profit = product_number * quantity_sold
else:
    print(f"Invalid input, please enter a valid number")
print(f"Your total profit for today is {total_profit:.2f}")
