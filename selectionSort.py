numbers = [4,1,2,3]

def selectionSort(array):
    indeX = 0
    indexValue = array[0]
    
    for i in range(len(array)-1,0,-1):
        for j in range(i):
            if array[j] > indexValue:
                indeX = j
                indexValue = array[j]
            #print(indeX, indexValue)
        
        temp = array[i]
        array[i] = array[indeX]
        array[indeX] = temp
        print(array)

print(numbers)
selectionSort(numbers)