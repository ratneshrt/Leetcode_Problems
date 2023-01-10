def median(nums1,nums2):
    nums = nums1 + nums2
    nums.sort()
    if len(nums)%2==0:
        indx = int(len(nums)/2)
        return float((nums[indx-2]+nums[indx])/2)
    else:
        indx = int(len(nums)+1/2)
        return float(nums[int(indx)-1])

num1 = [1,2]
num2 = [3,4]
print(median(num1,num2))