import requests
import json


url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url).json()
# print(json.dumps(response, indent=2))
print(response["value"])

# Part2
print("####### Part 2 #######")


city_name = input("Please enter the city name.")
# country_code = input("Please enter the country code.")
url2 = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=860bb330bc46d74511f5ed55ff8b4cf0"+"&units=metric"
response2 = requests.get(url2).json()
# print(json.dumps(response2, indent=3))
print("_____" + response2["name"] + "_____")
print("Weather Description:  " + response2["weather"][0]["description"])
f_temp = int(response2["main"]["temp"])
# print(f_temp)
# celsius = (f_temp - 273.15) * 9/5
# celsius_round = str(round(celsius, 1))

print("Temperature :" + str(f_temp))











