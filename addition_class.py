class Addition:
    def __init__(self, num1, num2):
        self.num1 = num1 + 3  # Adding 3 to num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2

# Instantiate the class and call the add method
addition_instance = Addition(5, 10)  # Create an object of Addition with num1=5, num2=10
print(addition_instance.add())  # Call the add method to print the result
