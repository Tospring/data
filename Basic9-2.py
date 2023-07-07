numbers=[[3,1],[1,2],[2,2],[1,1],[2,1]]
print(numbers)

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers.sort(key=lambda x:(-x[0],x[1]))
print(numbers)

print()
A = [['3','1'],['1','2'],['2','2'],['1','1'],['2','1']]
print(A)
A.sort(key=lambda x:x[1])
print(A)
A.sort(key=lambda x:x[0],reverse=True)
print(A)

