import string
from longdivider import LongDivisionMethods
from quadratic import Quadratic
from polynomial import Polynomial

import datetime
start_time = datetime.datetime.now()


def inputPolynomial():
    highestPower = int(input("What's the highest power of x? "))
    currentPower = highestPower
    coefficients = list()
    alphabet = string.ascii_lowercase

    model = "Your equation should be in the form: "

    for i in range(highestPower):
        model += f"{alphabet[i]}x^{highestPower - i} + "

    model += f"{alphabet[highestPower]}"

    print(model)

    for i in range(highestPower + 1):
        coefficient = int(input(f"{alphabet[i]}: "))
        coefficients.append(coefficient)
        
    return Polynomial(highestPower, coefficients)

while True:
    poly = inputPolynomial()

    factorConstant= poly.findFactor()
    print(factorConstant)

    quad = LongDivisionMethods.longDivide(poly, 1, factorConstant)
    print(quad.coefficients)
    quad.solve()
    
    print("You may need to simplify these solutions.")
    print("You're welcome btw")
    
    uInput = input("n = another problem, x = exit ")
    if (uInput == 'a'):
        continue
    elif (uInput == "x"):
        break
    
end_time = datetime.datetime.now()
print(end_time - start_time)