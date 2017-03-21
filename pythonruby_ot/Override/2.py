class Cal(object):
    _history = []
    def __init__(self, v1, v2): #constructor
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2

    def add(self):
        result = self.v1+self.v2
        Cal._history.append('add : %d+%d=%d' % (self.v1, self.v2, result))
        return
    def subtract(self):
        result = self.v1-self.v2
        Cal._history.append('sub : %d-%d=%d' % (self.v1, self.v2, result))
        return

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

    @classmethod
    def history(cls):
        for item in Cal._history:
            print(item)
    def info(self):
        return 'Cal => v1 : %d, v2 : %d' % (self.v1, self.v2)

class CalMultiply(Cal):
    def multiply(self):
        result = self.v1*self.v2
        Cal._history.append('mul : %d*%d=%d' % (self.v1, self.v2, result))
        return result
    def info(self):
        return 'CalMultiply => %s' % super().info() # super()=Cal()

class CalDivide(CalMultiply):
    def divide(self):
        result = self.v1/self.v2
        Cal._history.append('div : %d/%d=%d' % (self.v1, self.v2, result))
        return result
    def info(self):
        return 'CalDivide => %s' % super().info() # super()=CalMutiply()


c0 = Cal(30, 60)
print(c0.info())

c1 = CalMultiply(10, 10)
print(c1.info())

c2 = CalDivide(20, 10)
print(c2.info())
