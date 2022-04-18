x = [1, 2, 3, 4, 5]

def square(x):
    print(x)
    return x**2

res = map(square, x)
#print(res)
print(list(res))

res = map(str, x)
print(list(res))
