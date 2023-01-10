def numberOfCuts(n):
    if n==1:
        return 0
    elif (n%2) == 0:
        return int(n/2)
    else:
        return n