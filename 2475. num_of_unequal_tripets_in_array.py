def unequalTriplets(nums):
    n = len(nums)
    c = 0
    if len(nums) < 3:
        return 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                    c = c + 1
    return c