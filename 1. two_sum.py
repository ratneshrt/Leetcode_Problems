#Using dictionary

def twoSum(nums,target):

    #declaring a dictionary to keep track of all the values seen so far
    #in the value t o index (key value)
    visited_numbers = dict()

    for index, num in enumerate(nums):

        #subtracting the num from the target to search for its pair
        number_to_be_search = target - num

        #if the pair is found, return the index of the both numbers
        if number_to_be_search in visited_numbers:
            return [index, visited_numbers[number_to_be_search]]
        #otherwise we simply add it to out disctionary for future lookup
        else:
            visited_numbers[num] = index

nums = [2,7,3,15,11]
target = 9
print(twoSum(nums,target))