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
        input('Enter the number of kilograms (kg) of coffee: ')
    elif selection=='T' or selection=='t':
        input('Enter the number of tea boxes: ')
else:
    print('Invalid input, you should enter c/C or t/T')

# if coffeeammount>0:
#     print()
# if teaboxammounnt>0:
#
#
#
# coffee=input('Quantity of coffee should be > ')
# tea=input('Number of tea boxes should be > ')




