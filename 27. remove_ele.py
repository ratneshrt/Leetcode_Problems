def removeElement(nums,val):
    step  = 0
    while step < len(nums):
        if nums[step] == val:
            nums.pop(step)
            continue
        step+=1
    return len(nums)