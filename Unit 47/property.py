class Person:
    def __init__(self):
        self.__age = 0

    @property
    def age(self):           # getter
        return self.__age

    @age.setter
    def age(self, value):    # setter
        self.__age = value

james = Person()
james.age = 20      # 인스턴스.속성 형식으로 접근하여 값 저장
print(james.age)    # 인스턴스.속성 형식으로 값을 가져옴
