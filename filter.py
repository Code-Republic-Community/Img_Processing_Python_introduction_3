numbers = [-2, -1, 0, 1, 2]

positive_numbers = filter(lambda n: n > 0, numbers)

a = list(positive_numbers)
print(a)

def is_positive(n):
    return n > 0

b = list(filter(is_positive, numbers))
print(b)
