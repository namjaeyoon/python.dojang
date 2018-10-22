def number_generator():
    x = [1, 2, 3]
    for i in x:
        yield i

for i in number_generator():
    print(i)
