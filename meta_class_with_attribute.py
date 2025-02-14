class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['meta_attribute'] = 'This is added by the metaclass'
        return super().__new__(cls, name, bases, dct)

class A(metaclass=Meta):
    pass

print(type(A))
print(A.meta_attribute)
