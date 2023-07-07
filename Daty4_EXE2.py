from collections import deque

def isPalindrome(str):
    q = deque(str)
    string = list(str)
    
    while q:
        if q.popleft() != string.pop():
            return False
    return True

def isPalindrome2(str):
    string = list(str)
    for i in range(len(string)//2):
        if string[i] != string[len(string)-1-i]:
            return False
    return True

string = input()
result = isPalindrome2(string)
print(result)

"""
q = deque()
string = list(input())

for i in range(len(string)):
    q.append(string[i])

#print(q,string)
numString = len(string)
count = 0
for _ in range(len(string)):
    if q.popleft() == string.pop():
        count = count+1
        #print(count)

if count == numString:
    print(True)
else:
    print(False) 

string = list(input())
count = 0

for i in range(numString):
    if string[i] == string[numString-1-i]:
       count = count+1

if count == numString:
    print(True)
else:
    print(False)
    
"""