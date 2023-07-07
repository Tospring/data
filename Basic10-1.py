A = {'a':1, 2:3, 'fruit':['apple','orange']}
print(A)

del A['a']
del A['fruit']
A[3] = 7
A[1] = 10
print(A)

print(A.keys())

print(A.values())

print(A.items())

#Basic 10-2
print(sorted(A.items()))
A = {'1':10, '2':20}
B = {'2':30, '3':30, '4':40}
print(A, B)

print('A|B=', A|B)
print('B|A=', B|A)
print('A=',A)
print('B=',B)

A.update(B)
print(A)
print(B)