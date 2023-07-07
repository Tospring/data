from random import randint
from time import time

def swap(array,i,j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def bubble(array,i):
    for j in range(i):
        if array[j] > array[j+1]:
            swap(array,j,j+1)
        print(array)

def bubbleSort(array):
    for i in range(len(array)-1,0,1):
        bubble(array,i)
        print(array)

def bubbleSort2(array):
    for i in range(len(array)-1,0,1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            print(array)

def bubbleTest(numbers):
    start=time()
    bubbleSort2(numbers)
    end=time()
    return end-start

#if __name__ == '__main__':
numbers = [4,3,2,1]
print(numbers)
bubbleSort(numbers)
print(numbers)
print(int(bubbleTest(numbers))*1000)
    
            
            