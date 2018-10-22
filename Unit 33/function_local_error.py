def A():
    x = 10        # A의 지역 변수 x
    def B():
        x = 20    # x에 20 할당

    B()
    print(x)      # A의 지역 변수 x 출력

A()
