#
#
#
#
#
#
#
#
#
#
#
#
#

expressions = input().split(', ')

c = calc()
next(c)

for e in expressions:
    print(c.send(e))

c.close()
