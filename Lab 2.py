age = int(input('Enter Age:'))
yrs_service = int(input('Enter years of service:'))
print('Mana Corp. Retirement Eligibility Checker')
print('Age: '+str(age))
print('Years of Service: '+str(yrs_service))
if age>50:
    if age>=65 or yrs_service+age>=80:
        print(f'You are eligible for retirement with full pension benefits')
    else:
        print(f'You are eligible for retirement with discounted pension benifits')
else:
    print(f'You are not eligible for retirement')
