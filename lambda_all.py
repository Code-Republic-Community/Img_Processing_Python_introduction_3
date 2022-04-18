numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10]

even = lambda x: x % 2 == 0
result = [even(number) for number in numbers]

if any(result):
    print('At least single even is found')
else:
    print('There is no even number is found')

if all(result):
    print('All are even')
