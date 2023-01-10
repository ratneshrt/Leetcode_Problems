def containsNearbyDuplicate(nums,k):
    l = {}
    for i in range(len(nums)):
        if nums[i] not in l:
            l[nums[i]] = i
        else:
            if i-l[nums[i]] <= k:
                return True
            else:
                l[nums[i]] = i
    return False