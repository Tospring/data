
from random import randint
from time import time

numbers = []
length = [2500, 5000, 10000]

def bubbleSort2(array):
    for i in range(len(numbers)-1,0,-1):
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                tmp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = tmp
            #print(numbers)
        
for k in range(0,len(length)):
    for m in range(0,length[k])
        numbers.append(randint(1,length[k]))
    
    start = time()
    bubbleSort2(numbers)
    end = time()
    
    print(f'Time for {length[k]} is {(end-start)*1000:.3f}')



