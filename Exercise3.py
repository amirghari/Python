zender = input("Enter the size of the zender.")
if int(zender) < 42:
    size = 42 - int(zender)
    print("The fish is back to the lake and the caught fish was " + str(size) + " centimetres below.")
# PART2
cruiseClass = input("Enter the class of your cruise.")
if cruiseClass == "A":
    print("above the car deck, equipped with a window.")
elif cruiseClass == "LUX":
    print("upper-deck cabin with a balcony.")
elif cruiseClass == "B":
    print("windowless cabin above the car deck.")
elif cruiseClass == "C":
    print("windowless cabin below the car deck.")
else:
    print("Invalid Cabin Class.")
# Part3
gender = input("Enter your gender")
if gender == "male":
    hmValue = input("Enter your hemoglobin value")
    if 134 <= int(hmValue) <= 167:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is Not normal.")
elif gender == "female":
    hmValue = input("Enter your hemoglobin value")
    if 117 <= int(hmValue) <= 155:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is Not normal.")
else:
    print("Please type 'female' or 'male' as your gender.")
# Part4
year = input("Enter the year to determine whether it's a leap year or not.")
if int(year) % 4 == 0:
    print("This year is a leap year.")
elif int(year) % 100 == 0 and int(year) % 400 == 0:
    print("This year is a leap year.")
else:
    print("This year is not a leap year!")



