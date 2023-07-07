numbers = [[0 for _ in range(5)] for _ in range(3)]
print(numbers)

numbers[0][1] = 1
print(numbers)
print()

numbers2 = [[5*j+i for i in range(1,6)] for j in range(3)]
print(numbers2)
print()

from random import randint
from copy import deepcopy

numbers3 = [[randint(1,100) for _ in range(2)] for _ in range(5)]
print(numbers3)
#numbers4 = [a[:] for a in numbers3]
numbers4 = deepcopy(numbers3)
print(numbers3)
numbers3[0][0] = 1
print(numbers4)

