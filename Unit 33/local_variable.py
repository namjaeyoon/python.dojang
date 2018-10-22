def foo():
    x = 10      # foo의 지역 변수
    print(x)    # foo의 지역 변수 출력

foo()
print(x)        # 에러. foo의 지역 변수는 출력할 수 없음
