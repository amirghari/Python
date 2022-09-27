import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
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
        print(f"The location is {row[0]} in {row[1]}.")
    return




airport_id = input("ENTER ident")
get_location(airport_id)



