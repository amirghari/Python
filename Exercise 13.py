from flask import Flask, request
import math
app = Flask(__name__)
@app.route("/prime_number/<num>")
def prime_number(num):
    def primenumber(num):
        for i in range(2, int(math.sqrt(abs(num)))):
            if num % i == 0:
                return False
            else:
                return True

    response = {
        "Number": num,
        "isprime": primenumber(int(num))
    }
    return response


if __name__ == '__main__':
    app.run(use_reloader= True, host='127.0.0.1', port=5000)

# Part2



