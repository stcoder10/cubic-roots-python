from asyncio.windows_events import NULL
import math
class Polynomial:
    def __init__(self, highestPower: float, coefficients: list):
        self.highestPower = highestPower
        self.coefficients = coefficients

    def findFactor(self):
        factorConstant = 0
                
        for input in range(-20, 20):
            result = 0
            i = 0
            for coefficient in self.coefficients:
                powerAns = math.pow(input, self.highestPower - i)
                result += (powerAns * coefficient)
                i += 1
            if result == 0:
                if input <= 0:
                    input = math.fabs(input)
                    factorConstant = input
                else:
                    input = math.fabs(input)
                    factorConstant = input - 1
        return factorConstant
