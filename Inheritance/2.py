class Cal(object):
    def __init__(self,v1,v2): #constructor
        if isinstance(v1,int):
            self.v1=v1
        if isinstance(v2,int):
            self.v2=v2
    def add(self):
        return self.v1+self.v2
    def subtract(self):
        return self.v1-self.v2
    def setV1(self,v):
        if isinstance(v,int):
            self.value1=v1
    def getV1(self):
        return self.v1
    def setV2(self,v):
        if isinstance(v,int):
            self.value2=v2
    def getV2(self):
        return self.v2

class CalMultiply(Cal):
    def multiply(self):
        return self.v1*self.v2
class CalDivide(CalMultiply):
    def divide(self):
        return self.v1/self.v2

c1=CalMultiply(10,10)
print('c1',c1.add())
print('c1',c1.multiply())
c2=CalDivide(20,10)
print('c2',c2.add())
print('c2',c2.multiply())
print('c2',c2.divide())
