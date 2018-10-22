count = int(input('반복할 횟수를 입력하세요: '))

for i in range(count + 1):       # 0부터 증가하면서 count까지 반복(count + 1)
    if i % 2 == 0:               # i를 2로 나누었을 때 나머지가 0이면 짝수
        continue                 # 아래 코드를 실행하지 않고 건너뜀
    print(i)
