year = input("Enter the year to determine whether it's a leap year or not.")
if int(year) % 4 == 0:
    print("This year is a leap year.")
elif int(year) % 100 == 0 and int(year) % 400 == 0:
    print("This year is a leap year.")
else:
    print("This year is not a leap year!")