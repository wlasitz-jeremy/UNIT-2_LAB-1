print('--------------------------------------------------')
print('*** Welcome to the Beverage Wholesale Program ***')
print('--------------------------------------------------')
print('Please select type of purchase:')
print('C: Coffee Beans')
print('T: Tea Boxes')
selection=input('>>> ')
coffee_amount=0
tea_box_amount=0
discount_price=0
province_abbreviation=['ab','bc','mb','nb','nl','ns', 'on','pe','qc','sk','nt','nu','yt']
gst=0
province_abbreviation = str(province_abbreviation).upper()
if selection=='c' or selection=='C' or selection=='t' or selection=='T':
    if selection=='C' or selection=='c':
        coffee_amount=float(input('Enter the number of kilograms (kg) of coffee: '))
        if float(coffee_amount)<=0:
            print('Quantity of coffee should be > 0')
            exit()
        else:
            province_abbreviation=input('Please enter the 2-letter province abbreviation: ')
            price = float(coffee_amount) * 18.50
            if coffee_amount > 25:
                discount_price=float(price) * 0.90
            else:
                discount_price=price
    elif selection=='T' or selection=='t':
        tea_box_amount=float(input('Enter the number of tea boxes: '))
        if float(tea_box_amount)<=0:
            print('Quantity of tea boxes should be > 0')
            exit()
        else:
            province_abbreviation=input('Please enter the 2-letter province abbreviation: ')
            price=float(tea_box_amount) * 9
            if tea_box_amount>10:
                discount_price = float(price) * 0.85
            else:
                discount_price=price
else:
    print('Invalid input, you should enter c/C or t/T')
    exit()
tea_box_amount=tea_box_amount*20
if province_abbreviation==province_abbreviation:
    if province_abbreviation=='ab' or province_abbreviation=='bc':
        gst=discount_price * 0.05
    elif province_abbreviation=='on':
        gst=discount_price * 0.13
    else:
        gst=discount_price*0.15
else:
    print('Invalid input, you should enter correct Province Abbreviation')
    exit()
total_price=discount_price + gst
if selection=='c' or selection=='C':
    print(f'{"Product"}{"Qty(Bags/kg)":>15}{"Price before Disc":>20}{"Price after Disc":>20}{"GST":>20}{"Total Price":>20}')
    print(f'{"Coffee":>5}{coffee_amount:>14.2f}{price:>10.2f}{discount_price:>10.2f}{gst:>10.2f}{total_price:>10.2f}')
else:
    print(f'{"Product"}{"Qty(Bags/kg)":>15}{"Price before Disc":>20}{"Price after Disc":>20}{"GST":>20}{"Total Price":>20}')
    print(f'{"Tea":>5}{tea_box_amount:>14.2f}{price:>10.2f}{discount_price:>10.2f}{gst:>10.2f}{total_price:>10.2f}')
