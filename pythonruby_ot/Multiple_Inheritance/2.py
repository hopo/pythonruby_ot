class CalMultiply():
    def multiply(self):
        return self.v1*self.v2

class CalDivide():
    def divide(self):
        return self.v1/self.v2

class Cal(CalMultiply, CalDivide): #multiple inheritance
    def __init__(self,v1,v2): #constructor
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2

    def add(self):
        return self.v1+self.v2
    def subtract(self):
        return self.v1-self.v2

    def setV1(self, v):
        if isinstance(v, int):
            self.value1 = v1
    def getV1(self):
        return self.v1

    def setV2(self, v):
        if isinstance(v, int):
            self.value2 = v2
    def getV2(self):
        return self.v2

c = Cal(100, 10)
print(c.add())
print(c.multiply())
print(c.divide())
