def number_coroutine():
    x = None
    while True:
        x = (yield x)    # 코루틴 바깥에서 값을 받아오면서 바깥으로 값을 전달
        if x == 3:
            return x

def print_coroutine():
    while True:
        x = yield from number_coroutine()   # 하위 코루틴의 yield에 지정된 값을 다시 바깥으로 전달
        print('print_coroutine:', x)

co = print_coroutine()
next(co)

x = co.send(1)    # number_coroutine으로 1을 보냄
print(x)          # 1: number_coroutine의 yield에서 바깥으로 전달한 값
x = co.send(2)    # number_coroutine으로 2를 보냄
print(x)          # 2: number_coroutine의 yield에서 바깥으로 전달한 값
co.send(3)        # 3을 보내서 반환값을 출력하도록 만듦
