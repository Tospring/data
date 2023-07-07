"""
A = {1,2,3}
B = {1,5,6}
print(f'A:{A}')
#print(f'B:{B}')
B.update([3])
B.remove(6)
print(f'B:{B}')

U = A.union(B)
I = A.intersection(B)
D = A.difference(B)

print("Union:", U)
print("Intersection;",I)
print("Difference: ",D)
"""
A = [2,2,1,1,3]
A = list(set(A))
print(A)

