
from collections import deque

def time_to_buy_tickets(tickets: list[int], k: int):
    count = 0
    i = 0
    while True :
        i = i % len(tickets)
        if tickets[i] != 0 :
            tickets[i] = tickets[i]-1
            count += 1
            if tickets[k] == 0:
                break
        i += 1
    return(count)    

def time_to_buy_tickets2(tickets: list[int], k: int):
    time = 0;
    for i, num in enumerate(tickets):
        if i <= k:
            time += min(tickets[i],tickets[k])
        else:
            time += min(tickets[i], tickets[k]-1)
    return time

n, k = map(int, input().split())
tickets = list(map(int, input().split()))

print(time_to_buy_tickets2(tickets,k))

    

