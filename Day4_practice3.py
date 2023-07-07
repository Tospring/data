def StockSpan(stockList : list[int]):
    results = []
    cnt = 0
    for i in range(0,len(stockList)):
        cnt = 0
        for j in range(i,-1,-1):
            if stockList[i] >= stockList[j]:
                cnt += 1
            else:
                break
        results.append(cnt)
    return results

def StockSpan2(stockList : list[int]):
    print(stockList)
    results = []
    spans = []
    for i in range(1, len(stockList)):
        if not spans:
            spans.append(0)
        for _ in range(len(spans)):
            if stockList[i] > stockList[spans[-1]]:
                spans.pop()
        spans.append(i)
        #print(spans)
        if len(spans) == 1:
            results.append(1+spans[-1])
        else:
            results.append(spans[-1]-spans[-2])
    return results

def StockSpanSol(prices : list[int]):
    spans = [0]*len(prices)
    stack = []
    for i, price in enumerate(prices):
        while len(stack) > 0 and prices[stack[-1]] <= price:
            stack.pop()
        if len(stack) > 0 :
            spans[i] = i - stack[-1]
        else:
            spans[i] = i + 1
        stack.append(i)
    return spans

#n = int(input())
#stocks = list(map(int, input().split()))
n = 7
stocks = [7,11,8,6,3,7,9]
print(StockSpanSol(stocks))