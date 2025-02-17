class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name} with bases {bases}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    pass
