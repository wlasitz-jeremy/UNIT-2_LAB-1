# current_price=float(input('Enter the current price '))
# last_month_price=float(input('Enter the last months price '))
# change_of_price=current_price-last_month_price
# monthly_mortgage=float(current_price)*(0.051)/12
# print(f'Current price is: {current_price}\nChange of price since last month is: {change_of_price}\nEstimated monthly mortage is: {monthly_mortgage}')




# r = float(input('Enter radius '))
# h = float(input('Enter height '))
# pi=3.14
# volume=str(pi*(r**2)*h)
# area=str((2*pi)*h*r + pi*(r**2))
# print("Area="+area+"\nVolume="+volume)




# sd=float(input('Enter starting distance '))
# ed=float(input('Enter stopping distance '))
# st=float(input('Enter starting time '))
# et=float(input('Enter stopping time '))
# d=ed-sd
# t=et-st
# v1=sd/st
# v2=ed/et
# cv=float(v2)-float(v1)
# a=float(cv)/float(t)
# print(f'"Velocity="{v2}m/s\nAccelleration="{a}m/s**2')




# num = float(input('Enter a number'))
# if num % 2 == 0:
#     print(str(num) + ' is even')
#     print(str(num) + ' is absolute')
# else:
#     print(str(num) + " is odd")
#     print(str(num) + ' is not absolute')




# grd = int(input('Enter grade point'))
# if grd>90 and grd<=100:
#     print(f'A+')
# elif grd>85 and grd<=89:
#     print(f'A')
# elif grd>80 and grd<=84:
#     print(f'A-')
# elif grd>77 and grd<=79:
#     print(f'B+')
# elif grd>73 and grd<=76:
#     print(f'B')
# elif 70<grd<72:
#     print(f'B-')
# elif grd>67 and grd<=69:
#     print(f'C+')
# elif grd>63 and grd<=66:
#     print(f'C')
# elif grd>60 and grd<=62:
#     print(f'C-')
# elif grd>55 and grd<=59:
#     print(f'D+')
# elif grd>50 and grd<=54:
#     print(f'D')
# else:
#     print(f'F')




# yr = int(input('Enter year: '))
# if yr%4==0:
#     if yr%100==0 or yr%400==0:
#         print(f'{yr} is not a leap year')
#     else:
#         print(f'{yr} is a leap year')
# else:
#     print(f'{yr} is not a leap year')




# course = 'Python'
# print(f'{course:>20}')
# print(f'{course:<20}')
# print(f'{course:20}')
# print(f'{"Centered":^20}\n')
# cadtd= 1.2798
# usdtd= 0.940
# cadytd= 2.7843
# usdytd= 2.050
# changeusd= (usdtd-usdytd)
# changecad= (cadtd-cadytd)
# print(f'{"Date":^10}{"Rate":^20}')
# print(f'Cad Yesterday{cadytd:^17.4f}')
# print(f'Cad Today{cadtd:^24.4f}')
# print(f'Cad Change{changecad:^22.4f}')
# print(f'Usd Yesterday{usdytd:^16.4f}')
# print(f'Usd Today{cadtd:^24.4f}')
# print(f'Usd Change{changeusd:^22.4f}')
# num=2
# while num<=512:
#     print(num)
#     num+=2




# kpm=1.61
# print(f'{"MPH"}',f'{"KPH":>10}')
# print('==========',"==========")
# for mph in range(10,80,10):
#     kph=mph*kpm
#     print(f'{mph:10d}{kph:>10.0f}')
# for i in range (1,3):
#     for j in range (1,3):
#         print(f'{i}*{j}=',i*j)




# RC='Rock Climbing'
# print(RC[5:10])
# for height in range(0,len(RC)):
#     print(RC[height-8])
# height=0
# while height<len(RC):
#     print(RC[height])
#     height+=2
# print(RC.upper())
# print(RC.lower())
# course=input("Enter course name: ")
# alpha=0
# beta=0
# charlie=0
# for charlie in course:
#     if course.isalpha():
#         alpha+=1
#     else:
#         if course.isalnum():
#             beta+=1
# print(alpha,beta)




# names=('Joe', 'Ed', 'Fred')
# num=len(names)
# print(num)
# first=min(names)
# print(first)
# print(max(names))
# del names




# days=('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')
# print(days)
# weekdays=(f'Weekdays:{days[1:5]}')
# print(weekdays)
# weekends=(f'Weekends:{days[0]} {days[6]}')
# print(weekends)




# def show_welcome():
#     """ Function to show welcome message """
#     print("Hello to the library!")
# def display_books():
#     """ Function to display books """
#     print("Here are our books...")
# def issue_books():
#     """ Function to issue books """
#     print("This book is for you!")
# def return_books():
#     """ Function to return books """
#     print("Thank-you for returning the books!")
# print(f"{show_welcome.__doc__}\n"
#       f"{display_books.__doc__}\n"
#       f"{issue_books.__doc__}\n"
#       f"{return_books.__doc__}\n")
# show_welcome()
# display_books()
# issue_books()
# return_books()




# def total(value1,value2):
#     total=0
#     '''sum of numbers'''
#     total=int(value1)+int(value2)
#     print(f"The sum of the numbers is: {total}")
# value1=input("Enter first number: ")
# value2=input("Enter second number: ")
# print(total.__doc__)
# total(value1,value2)




# def student(name,mark1,mark2,mark3):
#     average_mark = 0
#     average_mark = (mark1 + mark2 + mark3) / 3
#     print(f"Your average mark is {average_mark}")
# name = str(input("Enter your name: "))
# mark1 = float(input("Enter your mark: "))
# mark2 = float(input("Enter your mark: "))
# mark3 = float(input("Enter your mark: "))
# student(name,mark1,mark2,mark3)




# def celsius_to_fahrenheit():
#     c = float(input(f"Input your temperature in Celsius: "))
#     f = (9/5)*c+32
#     print(f"Your temperature in Fahrenheit is {f:.1f}")
# def fahrenheit_to_celsius():
#     f = float(input(f"Input your temperature in Fahrenheit: "))
#     c = (f-32)*(5/9)
#     print(f"Your temperature in Celsius is {c:.1f}")
# celsius_to_fahrenheit()
# fahrenheit_to_celsius()




# category = {
#     1: 120.45,
#     2: 99.50,
#     3: 75.69,
#     4: 65.73,
#     5: 51.49
# }
# product_number = int(input('Enter product number:\n       ').strip())
# if product_number in category:
#     print(category[product_number])
# else:
#     print('Try Again')




# quantity_sold = int(input("Please enter the quantity sold:\n       ").strip())
# if quantity_sold < 0:
#     print("Sorry, you can't solve for negative quantity")
# else:
#     print(f"You sold {quantity_sold}")



# testfile = open('C://SAIT//Object Oriented Programming 1 CPRG-216//testfile.txt', mode='w')
# line = "Hello World\n","This is pretty cool\n","I kinda love coding!"
# testfile.writelines(line)
# testfile.close()
# testfile = open('C://SAIT//Object Oriented Programming 1 CPRG-216//testfile.txt', mode='r')
# content = testfile.read()
# print(content)
# testfile.close()
# file = open('C://SAIT//Object Oriented Programming 1 CPRG-216//testfile.txt', 'r')
# line = file.readline()
# while line != '':
#     line = line.strip()
#     print(line)
#     line = file.readline()
# file.close()




# import os
# cwd = os.getcwd()
# print(cwd)
# file_path = os.path.join(cwd, "example.txt")
# print(file_path)
# exists = os.path.exists(file_path)
# print(exists)
# os.mkdir('my_directory')
# import os
# file_name = input("Enter file name: ")
# if os.path.exists(file_name):
#     print("The file Exists")
# else:
#     print("The file does not exist")




# file = open('temp_file.csv', 'r')
# file.readline()
# totalmaxtemp = 0
# numbertemp = 0
# content = file.readline()
# while content != "":
#     items = content.rstrip().split(",")
#     maxstring = items[9]
#     if maxstring != "":
#         maxtemp = float(maxstring)
#         totalmaxtemp += maxtemp
#         numbertemp += 1
#         content = file.readline()
# file.close()
# average_temp = totalmaxtemp / numbertemp
# print(f"{average_temp:.2f}")




# def countdown(n):
#     n -= 1
#     if n == 0:
#         print(n)
#     else:
#         countdown(n)
# n = int(input("Please enter a number: "))
# countdown(n)






# def gcd(x, y):
#     if y == 0:
#         return x
#     else:
#         return gcd(y, x % y)
#
# n1 = int(input("Enter first positive number: "))
# n2 = int(input("Enter second positive number: "))
#
# result = gcd(n1, n2)
# print(f"The GCD is {result}")
