#a = input().split()
#print(a)

b = list(map(int,input().split()))
print(b)

b.append('TY YI')
print(b)

b.remove(60)
b.remove(40)
b.pop()
print(b)

c = input()
b.insert(0,c)
print(b)