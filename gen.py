def infinite():
    num = 0
    while num < 10:
        yield num
        yield num + 2
        num += 1


t = infinite()

for i in t:
    print('I:', i)


for i in infinite():
    print('G:', i)
