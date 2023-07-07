def seqBound(key, array,upper=False):
    returnValue = 0
    if upper == False:
        for i in range(len(array)):
            if key <= array[i]:
                returnValue = i
                break
            else:
                key > array[i]
                returnValue = len(array)
        return returnValue
    else:
        for i in range(len(array)):
            if key < array[i]:
                returnValue = i
                break
            else:
                returnValue = len(array)
                continue
        return returnValue

A = [1,2,2,3,3,3,3,5,6,6,6,7,7,7]
print('result:')
print()
limit = 10
for i in range(limit):
    print(f'{i:2d}',end=' ')
print()
for i in range(limit):
    print(f'---',end=' ')
print()

for i in range(limit):
    print(f'{seqBound(i,A):2d}',end=' ')
print()

for i in range(limit):
    print(f'{seqBound(i,A,True):2d}',end=' ')
print()
print()

A=[1]
print(seqBound(1,A))
print(seqBound(1,A,True))
print()

A=[]
print(seqBound(1,A))
print(seqBound(1,A,True))
