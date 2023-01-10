def generate(n):
    a = []
    for x in range(n):
        a.append([1])
        if x>1:
            for c in range(x-1):
                a[x].append(a[x-1][c]+a[x-1][c+1])
        
        if x>0:
            a[x].append(1)
    return a