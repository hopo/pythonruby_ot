class Cal(object):
    def __init__(self, v1, v2): #constructor
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

c1 = Cal(10,10)
print(c1.add())
print(c1.subtract())
c1.setV1('one') #no integer
c1.v2 = 30


"""
#R:
class Cal
    def initialize(v1,v2)
        @v1=v1
        @v2=v2
    end
    def add()
        return @v1+@v2
    end
    def subtract()
        return @v1-@v2
    end
    def setV1(v)
        if v.is_a?(Interger)
            @v1=v
        end
    end
    def getV1()
        return @v1
    end
end
c1=Cal.new(10,10)
p c1.add()
p c1.subtract
c1.setV1('one')
p c1.add()

"""
