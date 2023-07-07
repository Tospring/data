string = list(input())

snum1 = 0
snum2 =0

mnum1 = 0
mnum2 = 0

bnum1 = 0
bnum2 = 0

nums = 0

for _ in range(len(string)):
    temp = string.pop()
    if temp == '{':
       mnum1 += 1
    elif temp == '}':
        mnum2 += 1
    elif temp == '(':
        snum1 += 1
    elif temp == ')':
        snum2 += 1
    elif temp == '[':
        bnum1 += 1
    elif temp ==']':
        bnum2 += 1
    elif temp =='*':
        nums += 1  
    else:
        continue
if (snum1 == snum2) and (mnum1 == mnum2) and (bnum1 == bnum2):
    print('True')
else:
    print('False')