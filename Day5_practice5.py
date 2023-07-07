from collections import deque

n = int(input())

smap = []

for i in range(n):
    smap.append(list(input()))

obstacles = []

# Traverse the map by using a queue
# Suppose that we start from smap[i][j]

for i in range(n):
    for j in range(n):
        if smap[i][j] != '1' : continue
        que = deque()
        que.append((i,j))
        smap[i][j] = '2'
        cnt = 0

        while que: 
            r, s = que.popleft()
            cnt += 1
            for p, q in [(r-1,s), (r+1,s), (r, s-1), (r,s+1)]:
                # if (p,q) is not visited:
                if 0 <= p < n and 0 <= q <n and smap[p][q] == '1':
                    que.append((p,q))
                    smap[p][q] = '2'
        obstacles.append(cnt)

obstacles.sort()
print(len(obstacles))

for b in obstacles:
    print(b)
    
        