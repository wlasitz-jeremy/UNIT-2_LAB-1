print('--------------------------------------------------')
print('*** Welcome to the Berverage Wholesale Program ***')
print('--------------------------------------------------')
print('Please select type of purchace:')
print('C: Coffee Beans')
print('T: Tea Boxes')
selection=input('>>> ')
coffee_amount=0
tea_box_amount=0
province_abbreviation=0
gst=0
discount_price_coffee=0
discount_price_tea=0
if selection=='c' or selection=='C' or selection=='t' or selection=='T':
    if selection=='C' or selection=='c':
        coffee_amount=input('Enter the number of kilograms (kg) of coffee: ')
        if int(coffee_amount)<=0:
            print('Quantity of coffee should be > 0')
            exit()
        else:
            province_abbreviation=(input('Please enter the 2-letter province abbreviation: '))
    elif selection=='T' or selection=='t':
        tea_box_amount=input('Enter the number of tea boxes: ')
        if int(tea_box_amount)<=0:
            print('Quantity of tea boxes should be > 0')
            exit()
        else:
            input('Please enter the 2-letter province abbreviation: ')
else:
    print('Invalid input, you should enter c/C or t/T')
price_coffee=float(coffee_amount)*18.50
price_tea=float(tea_box_amount)*(20*0.45)
float(coffee_amount)
float(tea_box_amount)
float(price_coffee)
float(price_tea)
if float(coffee_amount)>25 or float(tea_box_amount)>10:
        if float(coffee_amount)>25:
           discount_price_coffee=price_coffee*0.90
        elif float(tea_box_amount)>10:
            discount_price_tea=price_tea*0.85
else:
    discount_price_coffee=price_coffee*1
    discount_price_tea=price_tea*1
float(discount_price_coffee)
float(discount_price_tea)
if province_abbreviation=='ab' or province_abbreviation=='Ab' or province_abbreviation=='AB' or province_abbreviation=='bc' or province_abbreviation=='Bc' or province_abbreviation=='BC' or province_abbreviation=='mb' or province_abbreviation=='Mb' or province_abbreviation=='MB' or province_abbreviation=='nb' or province_abbreviation=='Nb' or province_abbreviation=='NB' or province_abbreviation=='nl' or province_abbreviation=='Nl' or province_abbreviation=='NL' or province_abbreviation=='ns' or province_abbreviation=='Ns' or province_abbreviation=='NS' or province_abbreviation=='on' or province_abbreviation=='On' or province_abbreviation=='ON' or province_abbreviation=='pe' or province_abbreviation=='Pe' or province_abbreviation=='PE' or province_abbreviation=='qc' or province_abbreviation=='Qc' or province_abbreviation=='QC' or province_abbreviation=='sk' or province_abbreviation=='Sk' or province_abbreviation=='SK' or province_abbreviation=='nt' or province_abbreviation=='Nt' or province_abbreviation=='NT' or province_abbreviation=='nu' or province_abbreviation=='Nu' or province_abbreviation=='NU' or province_abbreviation=='yt' or province_abbreviation=='Yt' or province_abbreviation=='YT':
    if province_abbreviation=='ab' or province_abbreviation=='Ab' or province_abbreviation=='AB' or province_abbreviation=='bc' or province_abbreviation=='Bc' or province_abbreviation=='BC':
        float(gst)==price_coffee*1.05 or float(gst)==price_tea*1.05
    if province_abbreviation=='on' or province_abbreviation=='On' or province_abbreviation=='ON':
        float(gst)==price_coffee*1.13 or float(gst)==price_tea*1.13
total_price_coffee=discount_price_coffee + gst
total_price_tea=discount_price_tea + gst
if selection=='c' or selection=='C':
    print(f'{"Product":10}{"Qty(Bags/kg)":10}{"Price before Disc":10}{"Price after Disc":10}{"GST":10}{"Total Price":10}')
    print(f'{"Coffee":10}{coffee_amount:10.2f}{price_coffee:10.2f}{discount_price_coffee:10.2f}{gst:10.2f}{total_price_coffee:10.2f}')
else:
    print(f'{"Product":10}{"Qty(Bags/kg)":10}{"Price before Disc":10}{"Price after Disc":10}{"GST":10}{"Total Price":10}')
    print(f'{"Tea":10}{tea_box_amount:10.2f}{price_tea:10.2f}{discount_price_tea:10.2f}{gst:10.2f}{total_price_tea:10.2f}')
