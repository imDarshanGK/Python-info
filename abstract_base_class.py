from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def my_method(self):
        pass

class ConcreteClass(MyAbstractClass):
    def my_method(self):
        print("Method implemented in the subclass!")

instance = ConcreteClass()
instance.my_method()
