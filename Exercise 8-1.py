import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='root123',
    autocommit=True
)
#print(connection)
def get_location(id):
    location = "SELECT name, municipality FROM airport WHERE ident ='"+id+"'"
    cursor = connection.cursor()
    cursor.execute(location)
    result = cursor.fetchall()
    # print(f"The location is {result[1]}.")
    for row in result:
        print(f"The Airport is in  {row[0]} in {row[1]}.")
    return

airport_id = input("ENTER ident")
get_location(airport_id)

# PART 2

import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='root123',
    autocommit=True
)

def airport_finder(code):
    small_number = "SELECT name, iso_country,type FROM airport"
    small_number += " WHERE iso_country ='"+code+"'"" AND type = 'small_airport'"
    cursor = connection.cursor()
    cursor.execute(small_number)
    small_result = cursor.fetchall()
    print(f"{code} has {len(small_result)} small airports")
    # for row in small_result:
def heliport (code):
    heliNumber = "SELECT name, iso_country, type From airport"
    heliNumber += " WHERE iso_country ='"+code+"'"" AND type = 'heliport'"
    cursor = connection.cursor()
    cursor.execute(heliNumber)
    print(f"and {len(heliNumber)} heliports.")

country_code = input("Please Enter the Country Code.")
airport_finder(country_code)
heliport(country_code)



