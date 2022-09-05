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
