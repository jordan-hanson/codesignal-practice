# Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search for target in nums. If target exists, then return its index, otherwise, return -1.

# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

# Note:

# All elements in nums are unique.
# The length of nums will be <= 100
# The value of each element in nums will be in the range [1, 10000]
# [execution time limit] 4 seconds (py3)

# [input] array.integer nums

# [input] integer target

# [output] integer
def csBinarySearch(nums, target):
    min_index = 0
    max_index = len(nums) -1
    while min_index <= max_index:
        mid_idx = (min_index + max_index) // 2
        print("mid_idx", mid_idx)
        print("Middle value", nums[mid_idx])
        if target == nums[mid_idx]:
            print("mid index in target if", mid_idx)
            return mid_idx
        elif nums[mid_idx] < target:
            min_index = mid_idx + 1
            print("mid_idx in elf", mid_idx)
        else:
            max_index = mid_idx - 1
            print("max_index", max_index)
    if min_index != max_index:
        return -1
    print(min_index, max_index)
    return min_index