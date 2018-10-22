count = int(input('반복할 횟수를 입력하세요: '))

i = 0
while True:    # 무한 루프
    print(i)
    i += 1
    if i == count:    # i가 입력받은 값과 같을 때
        break         # 반복문을 끝냄
