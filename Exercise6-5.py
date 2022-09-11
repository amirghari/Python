def showList(intList):
    newList = []
    for i in intList:
        if i % 2 == 0:
            newList.append(i)
    print("Old list: ", intList)
    print("New list: ", newList)
predefList = [1,2,3,4,5,6,7,8,9,10]
showList(predefList)