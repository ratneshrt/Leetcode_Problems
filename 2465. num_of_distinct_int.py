def distinctAverages(nums):
    nums.sort()
    n,u = len(nums), set()
    for i in range(0,n//2):
        u.add((nums[i]+nums[n-i-1])/2)
    return len(u)