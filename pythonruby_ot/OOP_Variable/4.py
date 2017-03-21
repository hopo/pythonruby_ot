class C:
    def __init__(self, v):
        self.__value = v #do not write attribute '__'
    def show(self):
        print(self.__value)


c1 = C(10)
# print(c1.__value)
c1.show()
