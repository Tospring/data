def binBoundLoop(key, array,upper=False):
    left, right = 0, len(array)
    while left<right:
        mid = (left+right)//2
        if key < array[mid]:
            right = mid
        elif key > array[mid]:
            left = mid+1
        else:
            if upper == True:
                left = mid+1
            else:
                right = mid
    return left

A = [1,2,2,3,3,3,3,5,6,6,6,7,7,7]
print('binBoundLoop result:')
print()
limit = 10
for i in range(limit):
    print(f'{i:2d}',end=' ')
print()
for i in range(limit):
    print(f'---',end=' ')
print()

for i in range(limit):
    print(f'{binBoundLoop(i,A):2d}',end=' ')
print()

for i in range(limit):
    print(f'{binBoundLoop(i,A,True):2d}',end=' ')
print()
print()

A=[1]
print(binBoundLoop(1,A))
print(binBoundLoop(1,A,True))
print()

A=[]
print(binBoundLoop(1,A))
print(binBoundLoop(1,A,True))
