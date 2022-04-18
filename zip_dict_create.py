numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

zipped = zip(numbers, numbers)

for i in zipped:
    print(i)

list_data = list(zipped)
dict_data = dict(zipped)

#list(zip(range(5), range(100), strict=True))
#
##Traversing Lists in Parallel
#
for l, n in zip(letters, numbers):
    print(f'Letter: {l}')
    print(f'Number: {n}')

dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}

for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
    print(k1, '->', v1)
    print(k2, '->', v2)
