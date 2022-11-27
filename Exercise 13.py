from flask import Flask
import mariadb
import json

app = Flask(__name__)
@app.route("/prime_number/<num>")
def prime_number(num):
    def primenumber(num):
        if num == 2 or num == 3:
            return True
        else:
            for i in range(2, num):
                if num % i == 0:
                    return False
                    break
                elif i == (num-1):
                    return True
                    break

    response = {
        "Number": num,
        "isprime": primenumber(int(num))
    }
    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

# Part2

connection = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game2',
    user='root',
    password='root123'
)


@app.route('/airport/<string:icao>')
def get_airport(icao):
    try:
        sql = "SELECT name, municipality from airport where ident = '" + icao + "'"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        response = {
            "ICAO": icao,
            "Name:": result[0][0],
            "Location": result[0][1]
        }
        return response

    except ValueError:
        response = {
            "message": "Invalid number as entered",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

