def number_generator(stop):
    n = 0
    while n < stop:
        yield n
        n += 1

def three_generator():
    yield from number_generator(3)    # 숫자를 세 번 바깥으로 전달

for i in three_generator():
    print(i)
