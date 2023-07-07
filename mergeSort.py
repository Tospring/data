def merge(list1, list2, inc=1):
    result = []
    i, j = 0, 0
    while i<len(list1) or j<len(list2):
        if i == len(list1):
            result += list2[j:]
            break
        elif j == len(list2):
            result += list1[i:]
            break
        else:
            key1, key2 = list1[i], list2[j]
            if (inc and key1 < key2) or (inc==0 and key1>key2):
                result.append(key1)
                i += 1
            else:
                result.append(key2)
                j += 1
    print("merge",result)
    return result

def mergeSort(list, inc = 1):
    print(list)
    if len(list) <= 1:
        return list
    mid = len(list)//2
    left = mergeSort(list[:mid],inc)
    right = mergeSort(list[mid:],inc)
    return merge(left, right, inc)

A = [1,3,9,11,2,3,7,10]
print(mergeSort(A,1))