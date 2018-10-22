class Person
    def __init__(self)
        self.__age = 0

    def get_age(self)           # getter
        return self.__age
    
    def set_age(self, value)    # setter
        self.__age = value

james = Person()
james.set_age(20)
print(james.get_age())
