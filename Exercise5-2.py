number = input("please enter a number.")
list_number = []
while number != "":
    list_number.append(int(number))
    number = input("please enter a number.")
list_number.sort(reverse=True)
print(list_number)

