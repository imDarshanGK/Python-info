from xyz import Xyz, abstractmethod

class P(Xyz):
    @abstractmethod
    def calc(self):
        pass  # Implementation of calc would go here

class E(P):
    def calc(self):
        # Implementation of calc method for class E
        pass
