class Cal(object):
    """docstring for Cal."""
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2
    def add(self):
        return self.v1+self.v2
    def subtract(self):
        return self.v1-self.v2

c1 = Cal(10,10)
print(c1.add())
print(c1.subtract())

c2 = Cal(30,20)
print(c2.add())
print(c2.subtract())


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
end
c1=Cal.new(10,10)
p c1.add()
p c1.subtract()

c2.Cal.new(30,20)
p c2.add()
p c2.subtract()
"""
