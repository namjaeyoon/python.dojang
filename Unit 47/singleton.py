class Singleton(type):    # type을 상속받음
    __instances = {}      # 클래스의 인스턴스를 저장할 속성
    def __call__(cls, *args, **kwargs):    # 클래스로 인스턴스를 만들 때 호출되는 메서드
        if cls not in cls.__instances:     # 클래스로 인스턴스를 생성하지 않았는지 확인
            cls.__instances[cls] = super().__call__(*args, **kwargs)
                                           # 생성하지 않았으면 인스턴스를 생성하여 속성에 저장
        return cls.__instances[cls]        # 클래스로 인스턴스를 생성했으면 인스턴스 반환

class Hello(metaclass=Singleton):    # 메타클래스로 Singleton을 지정
    pass

a = Hello()     # 클래스 Hello로 인스턴스 a 생성
b = Hello()     # 클래스 Hello로 인스턴스 b 생성
print(a is b)   # True: 인스턴스 a와 b는 같음
