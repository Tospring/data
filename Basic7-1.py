import random
numbers = []
for _ in range(10):
    a = random.randint(1,10)
    numbers.append(a)
print('numbers:', numbers)
print(f'The sum is {sum(numbers)}.')

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

"""
b = list(map(int, input().split()))
for element in b:
    if element in numbers:
        print(element, 'is in the list.')
    else:
        print(element, 'is not in the list.')
"""
"""
number = int(input())
print(numbers.count(number),'occurrences of', number)
"""
"""
c = list(map(int, input().split()))
for element in c:
    if element in numbers:
        print(f'{element} is in numbers[{numbers.index(element)}]')
    else:
        print(element, 'is not in the list.')
"""

number = int(input())

occurrence = []

for i in range(len(numbers)):
    if number == numbers[i]:
        occurrence.append(i)
if occurrence == []:
    print(number, 'is not in the list.')
else:
    print(f'{number} is in the follwing locations {occurrence}.')

