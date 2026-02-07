print('--------------------------------------------------')
print('*** Welcome to the Berverage Wholesale Program ***')
print('--------------------------------------------------')
print('Please select type of purchace:')
print('C: Coffee Beans')
print('T: Tea Boxes')
selection = input('>>> ')
coffeeamount=0
teaboxamount=0
if selection=='c' or selection=='C' or selection=='t' or selection=='T':
    if selection=='C' or selection=='c':
        coffeeamount=input('Enter the number of kilograms (kg) of coffee: ')
        if int(coffeeamount)<=0:
            print('Quantity of coffee should be > 0')
            exit()
        else:
            province_abbreviation=(input('Please enter the 2-letter province abbreviation: '))
    elif selection=='T' or selection=='t':
        teaboxamount=input('Enter the number of tea boxes: ')
        if int(teaboxamount)<=0:
            print('Quantity of tea boxes should be > 0')
            exit()
        else:
            input('Please enter the 2-letter province abbreviation: ')
else:
    print('Invalid input, you should enter c/C or t/T')
price_coffee=float(coffeeamount)*18.50
price_tea=float(teaboxamount)*(20*0.45)
if int(coffeeamount)>25 or int(teaboxamount)>10:
        if coffeeamount>25:
           price_coffee=price_coffee*0.90
        elif teaboxamount>10:
            price_tea=price_tea*0.85
else:
    discount_coffee=price_coffee*1
    discount_tea=price_tea*1
if province_abbreviation=='ab' or province_abbreviation=='Ab' or province_abbreviation=='AB' or province_abbreviation=='bc' or province_abbreviation=='Bc' or province_abbreviation=='BC' or province_abbreviation=='mb' or province_abbreviation=='Mb' or province_abbreviation=='MB' or province_abbreviation=='nb' or province_abbreviation=='Nb' or province_abbreviation=='NB' or province_abbreviation=='nl' or province_abbreviation=='Nl' or province_abbreviation=='NL' or province_abbreviation=='ns' or province_abbreviation=='Ns' or province_abbreviation=='NS' or province_abbreviation=='on' or province_abbreviation=='On' or province_abbreviation=='ON' or province_abbreviation=='pe' or province_abbreviation=='Pe' or province_abbreviation=='PE' or province_abbreviation=='qc' or province_abbreviation=='Qc' or province_abbreviation=='QC' or province_abbreviation=='sk' or province_abbreviation=='Sk' or province_abbreviation=='SK' or province_abbreviation=='nt' or province_abbreviation=='Nt' or province_abbreviation=='NT' or province_abbreviation=='nu' or province_abbreviation=='Nu' or province_abbreviation=='NU' or province_abbreviation=='yt' or province_abbreviation=='Yt' or province_abbreviation=='YT':
    if province_abbreviation=='ab' or province_abbreviation=='Ab' or province_abbreviation=='AB' or province_abbreviation=='bc' or province_abbreviation=='Bc' or province_abbreviation=='BC':
        price_coffee*1.05 or price_tea*1.05
    if province_abbreviation=='on' or province_abbreviation=='On' or province_abbreviation=='ON':
        price_coffee*1.13 or price_tea*1.13

if selection=='c' or selection=='C':
    print('Product Coffee')
else:
    print(f'Product {"Tea":^10}')








