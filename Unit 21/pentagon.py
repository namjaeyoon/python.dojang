import turtle as t

t.shape('turtle')
for i in range(5):      # 오각형이므로 5번 반복
    t.forward(100)
    t.right(360 / 5)    # 360을 5로 나누어서 외각을 구함
