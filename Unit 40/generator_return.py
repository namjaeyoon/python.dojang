def one_generator():
    yield 1
    return 'return에 지정한 값'

try:
    g = one_generator()
    next(g)
    next(g)
except StopIteration as e:
    print(e)    # return에 지정한 값
