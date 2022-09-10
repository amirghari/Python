city_list = []
x = 5
for i in range(5):
    city = input("Enter the city name")
    city_list.append(city)
for i in range(5):
    print(city_list[5-x])
    x -= 1

