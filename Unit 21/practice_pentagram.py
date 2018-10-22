import turtle as t

n = 5
t.shape('turtle')
for i in range(n):
    t.forward(100)
    t.right((360 / n) * 2)
    t.forward(100)
    t.left(360 / n)
