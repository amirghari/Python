def evenMaker(lists):
    for list in lists:
        result = list % 2
        if (float(result) != 0):
            lists.remove(list)
    return lists




numberList = []
number = int(input("Enter a number to add it to the list. In case you want to stop enter 0. "))
while number != 0:
    numberList.append(number)
    number = int(input("Enter a number to add it to the list. In case you want to stop enter 0. "))
print(numberList)
print(evenMaker(numberList))