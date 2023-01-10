def pivotInteger(n):
    nums = []
    for k in range(1,n+1):
        nums.append(k)
    S = sum(nums)
    leftsum = 0
    for i, x in enumerate(nums):
        if leftsum == (S - leftsum - x):
            return i+1
        leftsum += x
    return -1