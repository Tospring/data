def merge(array1,array2,inc=1):
    newList = []
    i, j = 0, 0
    while i<len(array1) or j<len(array2):
        if i == len(array1):
            newList= newList + array2[j:]
            break
        elif j == len(array2):
            newList=newList + array1[i:]
            break
        
        if array1[i] <= array2[j]:
            newList.append(array1[i])
            i = i+1
        else:
            newList.append(array2[j])
            j = j+1
        #print(i, j)
        #print(newList)
    return newList

A = [1,3,9,11,2,3,7,10]
print(merge(A[0:4],A[4:len(A)]))
