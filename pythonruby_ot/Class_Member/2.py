class Cs:
    @staticmethod
    def static_method():
        print('Static method')

    @classmethod
    def class_method(cls):
        print('Class method')
    def instance_method(self):
        print('Instance method')

i = Cs()
Cs.static_method() #class static member
Cs.class_method() #class member
i.instance_method()
