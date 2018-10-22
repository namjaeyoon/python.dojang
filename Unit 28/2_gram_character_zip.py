text = 'hello'

two_gram = zip(text, text[1:])
for i in two_gram:
    print(i[0], i[1], sep='')
