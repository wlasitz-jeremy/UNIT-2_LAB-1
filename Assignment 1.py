print('--------------------------------------------------')
print('*** Welcome to the Berverage Wholesale Program ***')
print('--------------------------------------------------')
print('Please select type of purchace:')
print('C: Coffee Beans')
print('T: Tea Boxes')
selection = input('>>> ')
coffeeammount=0
teaboxammounnt=0
if selection=='c' or selection=='C' or selection=='t' or selection=='T':
    if selection=='C' or selection=='c':
        coffeeammount=input('Enter the number of kilograms (kg) of coffee: ')
        if int(coffeeammount)<=0:
            print('Quantity of coffee should be > 0')
        else:
            print(input('Please enter the 2-letter provine abbreviation: '))
    elif selection=='T' or selection=='t':
        teaboxammount=input('Enter the number of tea boxes: ')
        if int(teaboxammounnt)<=0:
            print('Quantity of tea boxes should be > 0')
        else:
            print(input('Please enter the 2-letter provine abbreviation: '))
else:
    print('Invalid input, you should enter c/C or t/T')









