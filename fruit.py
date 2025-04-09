class Fruit:
    def __init__(self):
        print('1')

class Apple(Fruit):
    def __init__(self, color="Red"):
        super().__init__()
        self.color = color
        print('2')

    def display_color(self):
        print(self.color)

# Create an Apple object
obj = Apple()
obj.display_color()  # Output: Red
