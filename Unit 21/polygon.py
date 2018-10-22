import turtle as t

n = int(input())        # 사용자의 입력을 받음
t.shape('turtle')
for i in range(n):      # n번 반복
    t.forward(100)
    t.right(360 / n)    # 360을 n으로 나누어서 외각을 구함
