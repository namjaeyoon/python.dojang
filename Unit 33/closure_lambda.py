def calc():
    a = 3
    b = 5
    return lambda x: a * x + b    # 람다 표현식을 반환

c = calc()
print(c(1), c(2), c(3), c(4), c(5))
