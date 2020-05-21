class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print(self.num1 + self.num2)

    def subtraction(self):
        print(self.num1 - self.num2)

    def multi(self):
        print(self.num1 * self.num2)

    def division(self):
        print(self.num1 / self.num2)

operator1 = Calculator(1,2)
operator1.add()
operator1.subtraction()
operator1.multi()
operator1.division()
