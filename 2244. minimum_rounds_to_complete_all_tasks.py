def minimumRounds(tasks):
    count = {}
    for i in tasks:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    res = 0
    for i,j in count.items():
        if j==1:
            return -1
        res += (j+2)//3
    return res