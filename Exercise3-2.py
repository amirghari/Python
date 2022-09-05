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