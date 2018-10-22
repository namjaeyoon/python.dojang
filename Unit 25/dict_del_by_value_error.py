x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

for key, value in x.items():
    if value == 20:    # 값이 20이면
        del x[key]     # 키-값 쌍 삭제

print(x)
