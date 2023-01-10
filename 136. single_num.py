def singleNumber(nums):
    uniqNum = 0
    for idx in nums:
        uniqNum ^= idx #concept of XOR
    return uniqNum