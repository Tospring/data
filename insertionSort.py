def insertionSort(array):
    for i in range(1,len(array)):
        keyvalue = array[i]
        index = i-1
        while index >=0 and keyvalue < array[index]:
            array[i] = array[index]
            index = index-1
            #print(i,index)
        array[index+1] = keyvalue
        print(array)

numbers = [4, 5, 2, 3, 6]
print(numbers)
print()

insertionSort(numbers)
print(numbers)