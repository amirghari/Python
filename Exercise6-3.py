times = int(input("Enter Gallons"))
def conversion(gallons):
    return gallons * 3.78
if times > 0:
    litter = conversion(times)
    print(f"conversion to Litter is {litter}")
else:
    print("Enter a positive number.")