import math
def calcPricePizza(diameter, price,name):
    areaPizza = math.pi * diameter * diameter
    print("The price per square meter of pizza",name,f": {price / (areaPizza * 0.0001):.3f}")
    return price / (areaPizza * 0.0001)
dia1 = float(input("Input the diameter of pizza 1 in cm: "))
price1 = float(input("Input the price of pizza 1 in euro: "))
dia2 = float(input("Input the diameter of pizza 2 in cm: "))
price2 = float(input("Input the price of pizza 2 in euro: "))
if calcPricePizza(dia1,price1,1) < calcPricePizza(dia2,price2,2):
    print("Pizza 1 is cheaper than pizza 2")
elif calcPricePizza(dia1,price1,1) > calcPricePizza(dia2,price2,2):
    print("Pizza 2 is cheaper than pizza 1")
else:
    print("Same price")