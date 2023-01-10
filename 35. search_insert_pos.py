def searchInsert(a,target):
    for i in range(len(a)):
        if target == a[i]:
            return i

    res = 0
    for j in range(len(a)):
        if target>a[j]:
            res+=1
    return res