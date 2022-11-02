from datetime import date
# Mooc Part 8-1
def smallest_average(first: dict, second: dict, third: dict):
    first_average = (first["result1"] + first["result2"] + first["result3"]) / 3
    second_average = (second["result1"] + second["result2"] + second["result3"]) / 3
    third_average = (third["result1"] + third["result2"] + third["result3"]) / 3
    if first_average < second_average and first_average < third_average:
        return first
    elif second_average < third_average and second_average < first_average:
        return second
    else:
        return third


person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}
print(smallest_average(person1, person2, person3))


# Mooc part 8-2


def row_sums(matrix: list):
    list1 = matrix[0]
    result1 = 0
    for item in list1:
        result1 += item
    list1.append(result1)
    matrix[0] = list1

    list2 = matrix[1]
    result2 = 0
    for item in list2:
        result2 += item
    list2.append(result2)
    matrix[1] = list2
    return matrix


my_matrix = [[1, 2], [3, 4]]
row_sums(my_matrix)
print(my_matrix)

# Mooc Part 9-1

def list_years(dates:list):
    years = []
    for date in dates:
        year = date.year
        years.append(year)
    years.sort()
    return years

date1 = date(2019, 2, 3)
date2 = date(2006, 10, 10)
date3 = date(1993, 5, 9)

years = list_years([date1, date2, date3])
print(years)



# Mooc Part 9-2




for i in range(1, shopping_list.number_of_items()+1):
    item = shopping_list.item(i)
    amount = shopping_list.amount(i)
    print(f"{item}: {amount} units")

if __name__ == "__main__":
    my_list = ShoppingList()
    my_list.add_item("bananas", 10)
    my_list.add_item("apples", 5)
    my_list.add_item("pineapple", 1)

    print(total_units(my_list))

