class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['greeting'] = 'Hello, World!'
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

obj = MyClass()
print(obj.greeting) 
