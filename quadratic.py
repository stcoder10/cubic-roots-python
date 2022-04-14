import math

class Quadratic:
    surdCoefficient = 1
    
    def __init__(self, coefficients:list):
        self.coefficients = coefficients
        self.surdIsRational = False
    
    def solve(self):
        a = self.coefficients[0]
        b = self.coefficients[1]
        c = self.coefficients[2]

        disc = b*b - 4*a*c

        surd = self.simplestSurdForm(disc)
        
        if self.surdIsRational:
            topOne = str(-b + surd)
            topTwo = str(-b - surd)
        else:
            topOne = f"{-b} + {surd}"
            topTwo = f"{-b} - {surd}"
        bottom = 2 * a
        
        print(f"Solution one: ({topOne}) / {bottom}")
        print(f"Solution two: ({topTwo}) / {bottom}")
        
            
        
    def simplestSurdForm(self, termToSqrt):
        imaginary = termToSqrt < 0
        if imaginary:
            re:float = termToSqrt * -1
        else:
            re:float = termToSqrt
            
        hasPerfectSquare = False
        coefficients = []
        coefficient = 1

        for i in range (2, int(re) + 1):
            quotient:float = re / i
            if quotient.is_integer():
                sqrt = math.sqrt(i)
                if sqrt.is_integer():
                    coefficients.append(sqrt)
                    re /= i
                    hasPerfectSquare = True
        
        if hasPerfectSquare:
            for j in coefficients:
                coefficient *= j
        
        if math.sqrt(re).is_integer():
            result = int(math.sqrt(re)) *coefficient
            if imaginary:                       
                return f"{result}i"
            else:
                self.surdIsRational = True
                return str(result)
        else:
            if imaginary:
                return f"{coefficient} * sqrt({re})i"
            else:
                return f"{coefficient} * sqrt({re})"