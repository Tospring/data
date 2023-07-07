a = ['*']*10
b = ['*' for i in range(10)]
c = ['*' for _ in range(10)]
print(a)

a[1] = '1'
a[2] = 2
a[3] = 3.0

print(a)

for i in range(1,10,2):
    a[i] = i
print(a)

even = a[0:10:2]
odd = a[1:10:2]
print(odd+even)