from abc import ABC , abstractmethod

class shape(ABC): #abstract class
    @abstractmethod
    def area(self):
        pass

class rectangle(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
    
class square(shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side*self.side
    
objs=[rectangle(4,5),square(2)]
for obj in objs:
    print(f"area:{obj.area()}")


