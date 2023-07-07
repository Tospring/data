from collections import deque

def number_of_employeees(employees: list[int], sandwiches: list[int]):
    Qemp = deque(emp)
    Qsan = deque(san)
    
    cnt = 0
    length = len(Qsan)

    while Qemp :
        print(cnt, len(Qsan), Qemp,Qsan)
        #cnt = cnt%len(Qsan)
        
        if Qemp[0] == Qsan[0] :
            Qsan.popleft()
            Qemp.popleft()
        else:
            Qemp.append(Qemp[0])
            Qemp.popleft()
        
        cnt += 1
        
        if cnt == length:
            if len(Qsan) == len(Qemp):
                break
            length = len(Qsan)
            cnt = 0
        
    return(len(Qemp))

def number_of_employees2(employees: list[int], sandwiches: list[int]):
    i, j = 0, 0
    cnt = 0
    index1, index2 = 0, 0
    
    for i in range(len(sandwiches)):
        for j in range(len(employees)):
            print(employees[index2], sandwiches[index1])
            if employees[index2] == sandwiches[index1]:
                print('Matched:')
                index1 = (index1 + 1)%len(sandwiches)
                index2 = (index2 +1)%len(employees)
                cnt += 1        
        
        index2 = (index2 + 1)%len(sandwiches)
                
    return(len(employees)-cnt)

def number_of_employees_Sol1(employees: list[int], sandwiches: list[int]):
    q = deque(employees)
    sandwiches = list(reversed(sandwiches))
    num = len(employees)
    iterations = 0
    
    while iterations < len(q):
        e = q.popleft()
        if e != sandwiches[-1] :
            q.append(e)
            iterations += 1
        else:
            sandwiches.pop()
            num -= 1
            iterations = 0
    return len(q)

def number_of_employees_Sol2(employees: list[int], sandwiches: list[int]):
    sandwiches = list(reversed(sandwiches))
    count = {0: 0, 1:0}
    for i in employees:
        count[i] += 1
    n = len(employees)
    k = 0
    while k < n and count[sandwiches[-1]] > 0:
        s = sandwiches[-1]
        sandwiches.pop
        count[s] -= 1
        k += 1
    return n-k
         


n = int(input())
emp = list(map(int, input().split()))
san = list(map(int, input().split()))

#print(number_of_employeees(emp, san))
print(number_of_employees2(emp,san))