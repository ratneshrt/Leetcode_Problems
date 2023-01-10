def minimumMoney(transactions):
    sum_diff = 0
    max_term = 0
        
    for cost, cashback in transactions:
        if cost > cashback:
            sum_diff += cost - cashback
            max_term = max(max_term, cashback)
        else:
            max_term = max(max_term, cost)

    return sum_diff + max_term