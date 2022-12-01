import math

class CompoundInterest:
    def __init__(self, principal, rate, time):
        self.principal = principal 
        self.rate = rate
        self.time = time
        self.num = 12

    def calculate_compound_interest(self, number):
        division = number.rate/self.num
        division += 1
        power = number.time*self.num
        inside_bracket = math.pow(division, power)
        a = number.principal*inside_bracket
        a_rounded = round(a, 2)
        return a_rounded

    def calculate_compound_interest_total(self, number):
        division = number.rate/self.num
        division += 1
        power = number.time*self.num
        inside_bracket = math.pow(division, power)
        a = (number.principal+60000)*inside_bracket
        a_rounded = round(a, 2)
        return a_rounded