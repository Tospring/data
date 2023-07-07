"""
numbers1 = []
numbers2 = []

for i in range(1,5):
    numbers1.append(i)
    print(numbers1)
print()

for i in range(1,5):
    numbers2.insert(0,5-i)
    print(numbers2)
print
"""

numbers = []
numbers1 = []
numbers2 = []

from random import randint
from time import time

size = 1000

for i in range(size):
    numbers.append(randint(0,size))

start = time()


for i in range(size*10^j):
    numbers1.append(numbers[i])
end = time()
print(f'Append time : {(end-start)*1000:.3f}')

start = time()
for i in range(size):
    numbers2.insert(0,numbers[i])
end = time()
print(f'Insert time : {(end-start)*1000:.3f}')



