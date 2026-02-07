print('--------------------------------------------------')
print('*** Welcome to the Berverage Wholesale Program ***')
print('--------------------------------------------------')
print('Please select type of purchace:')
print('C: Coffee Beans')
print('T: Tea Boxes')
selection = input('>>> ')
if selection=='c' or selection=='C' or selection=='t' or selection=='T':
    if selection=='C' or selection=='c':
        coffeeamount=input('Enter the number of kilograms (kg) of coffee: ')
        if int(coffeeamount)<=0:
            print('Quantity of coffee should be > 0')
        else:
            print(input('Please enter the 2-letter provine abbreviation: '))
    elif selection=='T' or selection=='t':
        teaboxamount=input('Enter the number of tea boxes: ')
        if int(teaboxamount)<=0:
            print('Quantity of tea boxes should be > 0')
        else:
            print(input('Please enter the 2-letter provine abbreviation: '))
else:
    print('Invalid input, you should enter c/C or t/T')









