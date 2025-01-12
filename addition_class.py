class addition:
    num1 = 23
    def __init__(self, num1, num2):
        self.num1 = num1+3
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
print(addition(5, 10))
