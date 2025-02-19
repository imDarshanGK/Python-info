from abd import aBc

class SimpleClass:
    def __init__(self):
        self.obj = aBc()

    def say_hello(self):
        print("Hello from SimpleClass!")

    def use_abc(self):
        self.obj.some_method()