numbers = [1, 2, 3, 4, 5, 6]
y = [x for x in numbers if x % 2 == 0]
print(y)

y = [2 **x for x in numbers]
print(y)

words = ['audi', 'bmw', 'alpharomeo', 'porshe', 'Mercedes']

words = [word.upper() if word.startswith('a') else word for word in words]
print(words)
