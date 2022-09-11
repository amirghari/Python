list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def sum_function(int_list):
    sumResult = 0
    for i in int_list:
        sumResult += i
    return sumResult

print("Sum of the list is: ",sum_function(list))