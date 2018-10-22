def coroutine(func):    # 코루틴 초기화 데코레이터
    def init(*args, **kwargs):
        co = func(*args, **kwargs)    # 코루틴 객체 생성
        next(co)                      # next 호출
        return co                     # 코루틴 객체 반환
    return init

@coroutine    # 코루틴 초기화 데코레이터 지정
def sum_coroutine():
        total = 0
        while True:
            x = (yield total)
            total += x

co = sum_coroutine()    # 코루틴 객체를 생성한 뒤 바로 사용

print(co.send(1))
print(co.send(2))
print(co.send(3))
