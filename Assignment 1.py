print(f'{'-'*47}\n{'*'*3}{"Welcome to the Beverage Wholesale Program"}{'*'*3}\n{'-'*47}\n{'Please select type of purchase:'}\n{'C: Coffee Beans'}\n{'T: Tea Boxes'}')
selection=input('>>> ')
coffee_amount=0
tea_box_amount=0
discount_price=0
price=0
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
    print(f'{'-'*110}\n{"Product":>8}{"Qty(Bags/kg)":>16}{"Price before Disc":>22}{"Price after Disc":>24}{"GST":>14}{"Total Price":>21}\n'
          f'{"Coffee":>8}{coffee_amount:>12.2f}{price:>20.2f}{discount_price:>25.2f}{gst:>20.2f}{total_price:>18.2f}\n'
          f'{'-'*110}')
else:
    print(f'{'-'*110}\n'
          f'{"Product":>8}{"Qty(Bags/kg)":>16}{"Price before Disc":>22}{"Price after Disc":>24}{"GST":>14}{"Total Price":>21}\n'
          f'{"Tea":>6}{tea_box_amount:14.2f}{price:>20.2f}{discount_price:>25.2f}{gst:>20.2f}{total_price:>18.2f}\n'
          f'{'-'*110}')
