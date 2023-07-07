
def commuterBuses(b: list[int], num):
    cnt = 0
    tmp = []
    for i in range(num):
        for j in range(i+1,num):
            if b[i] < b[j]:
                for k in  range(j+1,num):
                    if b[i] > b[k]:
                        cnt += 1
                        #print(i+1, j+1, k+1, b[i], b[j], b[k])
    return cnt

def commuterBuses2(b: list[int], num):
    ans = 0
    for i in range(num):
        cnt = 0
        for j in range(i+1,num):
            if b[i] < b[j]:
               #cnt(j')
               cnt += 1
            else:  #b[i] > b[j']  # ans += cnt(j')
                ans += cnt
    return ans 
#n = int(input())
#buses = list(map(int, input().split()))

n = 4
buses = [4, 2, 5, 3]
print(commuterBuses(buses, n))
print(commuterBuses2(buses,n))
