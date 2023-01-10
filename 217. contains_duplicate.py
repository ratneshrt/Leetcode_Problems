def containsDuplicate(nums):
    curr, count = nums[0], 0
    for i in range(len(nums)):
        if curr == nums[i]:
            count +=1
        else:
            curr = nums[i]
    if count >= 2:
        return True
    else:
        return False