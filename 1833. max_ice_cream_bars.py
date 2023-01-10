def maxIceCream(costs,coins):
    costs.sort()
    res = 0
    sum1 = 0
    for i in range(len(costs)):
        sum1 = sum1 + costs[i]
        while coins>=sum1:
            res += 1
            break
    return res