from quadratic import Quadratic
from polynomial import Polynomial

class LongDivisionMethods:
    def longDivide(poly: Polynomial, divCoefficient, divConstant):
        class Binomial: #class to store two term polynoimals
            def __init__(self, firstCoefficient, firstPower, secondCoefficient,
                        secondPower):
                self.firstCoefficient = firstCoefficient
                self.firstPower = firstPower
                self.secondCoefficient = secondCoefficient
                self.secondPower = secondPower

            def string(self):
                return (
                    f"{self.firstCoefficient} x ^ {self.firstPower} {self.secondCoefficient} x ^ {self.secondPower}"
                )


        def subtractBinBinomials(top:Binomial, bottom:Binomial):
            return Binomial(top.secondCoefficient - bottom.secondCoefficient,
                            currentPower, coefficients[i], currentPower - 1)


        def findRemainder(top:Binomial, bottom:Binomial):
            return top.secondCoefficient - bottom.secondCoefficient

        answerCoefficients = []
        highestPower = poly.highestPower
        currentPower = highestPower
        coefficients = poly.coefficients

        currentNumerator =Binomial(coefficients[0], currentPower, coefficients[1],
                                    currentPower - 1)

        working = True
        i = 0
        result = ""

        while working:
            resultCoefficient = currentNumerator.firstCoefficient / divCoefficient
            resultPower = currentPower - 1
            result += f"{resultCoefficient} x^{resultPower} + "
            answerCoefficients.append(resultCoefficient) 

            i += 1
            currentPower -= 1

            top =Binomial(resultCoefficient, currentPower, coefficients[i],
                            currentPower - 1)
            bottom =Binomial((resultCoefficient * divCoefficient), currentPower,
                                resultCoefficient * divConstant, currentPower - 1)

            if currentPower != 0:
                currentNumerator = subtractBinBinomials(top, bottom)

            else:
                working = False
                print()
                print("Remainder = " + str(findRemainder(top, bottom)))

        stringsToRemove = ["x^0 +", "^1", "+ -"]

        formattedResult = ((result.replace(stringsToRemove[0], "")).replace(
            stringsToRemove[1], "")).replace(stringsToRemove[2], "-")

        print(formattedResult)
        return Quadratic(answerCoefficients)
