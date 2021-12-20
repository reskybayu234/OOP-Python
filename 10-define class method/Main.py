class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def create_anonymous(cls):
        print("bayu")

bayu = Person("bayu",24)
bayu.create_anonymous()